
"""Retail Sales Data Analyzer"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

DATA_FILE = "retail_sales.csv"
OUTPUT_FOLDER = "output"


def press_enter():
    input("\nPress Enter to continue...")


class RetailAnalyzer:

    def __init__(self):
        self.data = None
        self.filtered_data = None
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # Load and clean CSV data
    def load_data(self, file_path):
        try:
            data = pd.read_csv(file_path)

            required = [
                "Date", "Product", "Category",
                "Price", "Quantity Sold", "Total Sales"
            ]

            missing = [col for col in required if col not in data.columns]

            if missing:
                print("Missing columns:", ", ".join(missing))
                return False

            print("\n--- Data Quality Check ---")
            print("Rows before cleaning:", len(data))
            print("Duplicate rows:", data.duplicated().sum())
            print("Missing values:\n", data.isnull().sum())

            data = data.drop_duplicates().copy()
            data["Date"] = pd.to_datetime(
                data["Date"], errors="coerce"
            )

            for col in ["Price", "Quantity Sold", "Total Sales"]:
                data[col] = pd.to_numeric(
                    data[col], errors="coerce"
                )

            for col in ["Product", "Category"]:
                data[col] = data[col].astype("string").str.strip()

            data = data.dropna(subset=required)

            data = data[
                (data["Price"] >= 0)
                & (data["Quantity Sold"] >= 0)
                & (data["Product"] != "")
                & (data["Category"] != "")
            ].copy()

            # Calculate sales from price and quantity
            data["Total Sales"] = (
                data["Price"] * data["Quantity Sold"]
            )

            data = data.sort_values("Date").reset_index(drop=True)

            if data.empty:
                print("No valid data remains after cleaning.")
                return False

            self.data = data
            self.filtered_data = data.copy()

            print("\nRows after cleaning:", len(data))
            print("Unique products:", data["Product"].nunique())
            print("Products:", data["Product"].unique().tolist())
            print("\nFirst five rows:")
            print(data.head().to_string(index=False))
            print("\nData loaded successfully!")
            return True

        except FileNotFoundError:
            print("CSV file not found:", file_path)
        except (pd.errors.EmptyDataError, pd.errors.ParserError) as error:
            print("CSV reading error:", error)
        except Exception as error:
            print("Error:", error)

        return False

    # Check whether data is available
    def check_data(self):
        if self.filtered_data is None or self.filtered_data.empty:
            print("No data available. Please load a valid CSV.")
            return False
        return True

    # Display dataset information
    def display_summary(self):
        if not self.check_data():
            return

        data = self.filtered_data

        print("\n--- Dataset Summary ---")
        print("Number of rows:", len(data))
        print("Number of columns:", len(data.columns))
        print("Columns:", data.columns.tolist())

        print(
            "Date range:",
            data["Date"].min().date(),
            "to",
            data["Date"].max().date()
        )

        print("\nData types:")
        print(data.dtypes)

        print("\nStatistical information:")
        print(
            data[["Price", "Quantity Sold", "Total Sales"]]
            .describe().round(2)
        )

    # Calculate sales metrics
    def calculate_metrics(self):
        if not self.check_data():
            return

        data = self.filtered_data

        product_sales = (
            data.groupby("Product")["Total Sales"]
            .sum().sort_values(ascending=False)
        )

        category_sales = (
            data.groupby("Category")["Total Sales"]
            .sum().sort_values(ascending=False)
        )

        print("\n========== SALES SUMMARY ==========")
        print(f"Total sales: ₹{data['Total Sales'].sum():,.2f}")
        print(f"Average sale: ₹{data['Total Sales'].mean():,.2f}")
        print(f"Total quantity sold: {data['Quantity Sold'].sum():,.0f}")
        print("Unique products:", data["Product"].nunique())

        if not product_sales.empty:
            print(
                "Best-selling product:",
                product_sales.index[0],
                f"(₹{product_sales.iloc[0]:,.2f})"
            )

        if not category_sales.empty:
            print(
                "Top category:",
                category_sales.index[0],
                f"(₹{category_sales.iloc[0]:,.2f})"
            )

        print("\nSales by category:")
        print(category_sales.to_string())

        print("\nTop 5 products:")
        print(product_sales.head(5).to_string())

        sales_array = data["Total Sales"].to_numpy()
        print(
            "Sales standard deviation (NumPy):",
            f"₹{np.std(sales_array):,.2f}"
        )

    # Filter data
    def filter_data(self):
        if not self.check_data():
            return

        print("\n1. Filter by category")
        print("2. Filter by date range")
        print("3. Reset filters")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            categories = sorted(
                self.data["Category"].dropna().unique().tolist()
            )

            print("Available categories:", categories)
            selected = input("Enter category: ").strip()

            result = self.data[
                self.data["Category"].str.casefold()
                == selected.casefold()
            ]

            if result.empty:
                print("No records found.")
            else:
                self.filtered_data = result.copy()
                print(result.head(15).to_string(index=False))

        elif choice == "2":
            try:
                start = pd.to_datetime(
                    input("Start date (YYYY-MM-DD): ").strip()
                )
                end = pd.to_datetime(
                    input("End date (YYYY-MM-DD): ").strip()
                )

                if start > end:
                    print("Start date must not be after end date.")
                    return

                result = self.data[
                    self.data["Date"].between(start, end)
                ]

                if result.empty:
                    print("No records found in this date range.")
                else:
                    self.filtered_data = result.copy()
                    print(result.head(15).to_string(index=False))

            except (ValueError, TypeError):
                print("Invalid date. Use YYYY-MM-DD.")

        elif choice == "3":
            self.filtered_data = self.data.copy()
            print("Filters reset successfully.")

        else:
            print("Invalid choice.")

    # Create charts
    def create_chart(self):
        if not self.check_data():
            return

        print("\n========== CHART MENU ==========")
        print("1. Top 10 products by sales")
        print("2. Sales by category")
        print("3. Sales over time")
        print("4. Correlation heatmap")

        choice = input("Choose chart type: ").strip()
        data = self.filtered_data
        sns.set_theme(style="whitegrid")

        try:
            if choice == "1":
                summary = (
                    data.groupby("Product")["Total Sales"]
                    .sum()
                    .sort_values(ascending=False)
                    .head(10)
                )

                if summary.empty:
                    print("No product data to display.")
                    return

                # Display products as separate horizontal bars
                summary = summary.sort_values(ascending=True)

                plt.figure(
                    figsize=(10, max(5, len(summary) * 0.6))
                )

                bars = plt.barh(
                    summary.index.astype(str),
                    summary.values
                )

                plt.title(
                    f"Top {len(summary)} Products by Total Sales"
                )
                plt.xlabel("Total Sales (₹)")
                plt.ylabel("Product")
                plt.bar_label(bars, fmt="₹%.0f", padding=3)
                filename = "sales_by_product.png"

            elif choice == "2":
                summary = (
                    data.groupby("Category")["Total Sales"]
                    .sum().sort_values(ascending=False)
                )

                if summary.empty:
                    print("No category data to display.")
                    return

                plt.figure(figsize=(9, 5))
                bars = plt.bar(
                    summary.index.astype(str), summary.values
                )

                plt.title("Total Sales by Category")
                plt.xlabel("Category")
                plt.ylabel("Total Sales (₹)")
                plt.xticks(rotation=30, ha="right")
                plt.bar_label(bars, fmt="₹%.0f", padding=3)
                filename = "sales_by_category.png"

            elif choice == "3":
                summary = (
                    data.groupby("Date")["Total Sales"]
                    .sum().sort_index()
                )

                if summary.empty:
                    print("No date data to display.")
                    return

                plt.figure(figsize=(10, 5))
                plt.plot(
                    summary.index,
                    summary.values,
                    marker="o"
                )

                plt.title("Sales Over Time")
                plt.xlabel("Date")
                plt.ylabel("Total Sales (₹)")
                plt.xticks(rotation=30, ha="right")
                plt.grid(True, linestyle="--", alpha=0.5)
                filename = "sales_over_time.png"

            elif choice == "4":
                numeric_data = data[
                    ["Price", "Quantity Sold", "Total Sales"]
                ]

                if len(numeric_data) < 2:
                    print("At least two rows are required.")
                    return

                plt.figure(figsize=(7, 5))
                sns.heatmap(
                    numeric_data.corr(),
                    annot=True,
                    cmap="coolwarm",
                    fmt=".2f"
                )

                plt.title("Sales Correlation Heatmap")
                filename = "sales_correlation_heatmap.png"

            else:
                print("Invalid chart choice.")
                return

            plt.tight_layout()

            file_path = os.path.join(OUTPUT_FOLDER, filename)
            plt.savefig(file_path, dpi=150, bbox_inches="tight")
            plt.show()
            plt.close()

            print("Chart saved successfully:", file_path)

        except Exception as error:
            plt.close("all")
            print("Could not create chart:", error)

    # Main menu
    def run(self):
        path = input(
            f"Enter CSV path (Enter for {DATA_FILE}): "
        ).strip() or DATA_FILE

        self.load_data(path)

        while True:
            print("\n========== MAIN MENU ==========")
            print("1. Load / reload CSV")
            print("2. View dataset summary")
            print("3. Calculate sales metrics")
            print("4. Filter data")
            print("5. Create chart")
            print("6. Exit")

            choice = input("Enter choice (1-6): ").strip()

            if choice == "1":
                new_path = input(
                    f"CSV path (Enter for {DATA_FILE}): "
                ).strip() or DATA_FILE
                self.load_data(new_path)
                press_enter()

            elif choice == "2":
                self.display_summary()
                press_enter()

            elif choice == "3":
                self.calculate_metrics()
                press_enter()

            elif choice == "4":
                self.filter_data()
                press_enter()

            elif choice == "5":
                self.create_chart()
                press_enter()

            elif choice == "6":
                print("Thank you for using Retail Sales Data Analyzer!")
                break

            else:
                print("Invalid choice. Enter a number from 1 to 6.")
                press_enter()


def main():
    print("=" * 42)
    print("       RETAIL SALES DATA ANALYZER")
    print("=" * 42)

    analyzer = RetailAnalyzer()
    analyzer.run()


if __name__ == "__main__":
    main()

