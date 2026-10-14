# 📊 Retail Sales Data Analyzer

## 📌 Project Overview

**Retail Sales Data Analyzer** is a Python-based data analysis project designed to analyze retail sales data, identify sales trends, and present meaningful insights through data visualization.

The project uses Python libraries such as Pandas, NumPy, Matplotlib, and Seaborn to process sales records, calculate important business metrics, and generate graphical reports. It provides a simple menu-driven interface that allows users to load CSV data, explore sales information, filter records, and visualize results.

## 🎯 Project Objectives

- Analyze retail sales data using Python.
- Clean datasets by identifying missing values, invalid records, and duplicate rows.
- Calculate total sales, average sales, and product-wise sales performance.
- Identify the best-selling products and top-performing categories.
- Filter sales records by product category and date range.
- Visualize sales performance through different types of charts.
- Generate useful insights to support data-driven decision-making.

## ✨ Key Features

### 📂 CSV Data Management
- Load retail sales data from a CSV file.
- Validate required columns before analysis.
- Identify missing values and duplicate records.
- Handle invalid dates and numerical values.
- Display the first few records after data cleaning.

### 📈 Sales Analysis
- Calculate total revenue and average sales.
- Analyze total quantity sold.
- Identify the best-selling product.
- Compare sales across product categories.
- Calculate sales standard deviation using NumPy.
- Display descriptive statistics for numerical columns.

### 🔎 Data Filtering
- Filter records by product category.
- Select records within a specific date range.
- Reset filters to return to the complete dataset.

### 📊 Data Visualization
The project generates four types of visualizations:

- **Product Sales Bar Chart:** Displays the top 10 products according to total sales.
- **Category Sales Bar Chart:** Compares total sales across product categories.
- **Sales Trend Line Chart:** Shows how sales change over time.
- **Correlation Heatmap:** Visualizes relationships between numerical sales-related variables.

Generated charts are saved in the output folder for future reference.

### 🖥️ Interactive Menu
- Simple menu-driven program.
- Separate options for data loading, analysis, filtering, and chart creation.
- Basic error handling for common input and file-related problems.
- Press Enter to continue between menu operations.

## 🛠️ Technologies Used

- **Python** — Main programming language.
- **Pandas** — Data cleaning, filtering, grouping, and analysis.
- **NumPy** — Numerical calculations and statistical operations.
- **Matplotlib** — Creation of bar charts and line graphs.
- **Seaborn** — Heatmap generation and chart styling.
- **CSV** — Storage and input of retail sales records.

## 📁 Project Structure

- `retail_analyzer.py` — Main Python application.
- `retail_sales.csv` — Sample retail sales dataset.
- `requirements.txt` — Required Python libraries.
- `output/` — Folder containing generated chart images:
  - `sales_by_product.png`
  - `sales_by_category.png`
  - `sales_over_time.png`
  - `sales_correlation_heatmap.png`

## ⚙️ Installation and Setup

1. Install Python on your computer.
2. Download or clone this repository.
3. Open the project folder in Visual Studio Code or another Python editor.
4. Install the required libraries listed in the requirements file.
5. Ensure the CSV dataset is available in the project folder.
6. Run the main Python application.
7. Follow the on-screen menu to analyze the data and generate charts.

## 📋 Dataset Requirements

The CSV dataset should contain the following columns:

- **Date:** Date of the sales transaction.
- **Product:** Name of the product.
- **Category:** Product category.
- **Price:** Price per unit.
- **Quantity Sold:** Number of units sold.
- **Total Sales:** Total sales value for the transaction.

The application recalculates total sales using price and quantity after cleaning the data.

Users can also provide their own CSV file, provided it follows the required column structure.

## 📊 Expected Output

After running the project, users can explore sales summaries, product rankings, category comparisons, and date-based trends. The application also generates visual charts and saves them in the output folder.

These results help users understand product performance, compare categories, and identify patterns in retail sales data.

## 🎓 Learning Outcomes

This project demonstrates practical applications of Python programming, object-oriented programming, data cleaning, Pandas data manipulation, NumPy calculations, statistical analysis, and data visualization.

It is suitable for students learning data analytics and Python-based business analysis.

## 🚀 Future Enhancements

- Add an interactive graphical dashboard.
- Include monthly and yearly sales growth analysis.
- Export sales summaries to Excel or PDF.
- Add profit and loss analysis.
- Integrate database support.
- Develop predictive sales analysis using machine learning.

## 👨‍💻 Project Information

**Project Name:** Retail Sales Data Analyzer

**Project Type:** Python Data Analytics Project

**Domain:** Retail Analytics and Data Visualization

**Purpose:** Educational and practical learning

---

⭐ If you find this project useful, consider giving the repository a star on GitHub.

**Made with Python, Pandas, NumPy, Matplotlib, and Seaborn.**
