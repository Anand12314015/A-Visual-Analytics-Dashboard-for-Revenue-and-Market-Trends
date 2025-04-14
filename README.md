# Sales Data Analysis Project

## Overview
This project performs a comprehensive analysis of sales data to derive meaningful insights about business performance, product trends, and regional distribution. The analysis includes various visualizations to track sales growth, identify best-selling products, analyze seasonal patterns, evaluate regional performance, and forecast sales trends.

## Features
- Monthly Sales Growth Tracking
- Best-Selling Products Analysis
- Seasonal Sales Pattern Analysis
- Regional Performance Evaluation
- Sales Forecasting Insights

## Requirements
- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn

## Installation
1. Clone this repository
2. Install the required packages:
```bash
pip install pandas numpy matplotlib seaborn openpyxl
```

## Data Source
The analysis uses an Excel file (`sales_dataset.xlsx`) containing sales data with the following key columns:
- Date
- Product Name
- Total Revenue
- Customer Region

## Analysis Components

### 1. Monthly Sales Growth
- Visualizes total revenue trends over time using a bar plot
- Helps track business growth and identify peak sales periods

### 2. Best-Selling Products
- Identifies top 5 products by total revenue
- Uses line plot to show revenue distribution across products

### 3. Seasonal Sales Analysis
- Analyzes sales patterns across different months
- Uses scatter plot to visualize monthly revenue distribution

### 4. Regional Performance
- Evaluates sales distribution across different regions
- Uses pie chart to show revenue share by region

### 5. Sales Forecasting
- Provides historical distribution of monthly revenue
- Uses histogram with KDE to show revenue patterns

## Usage
1. Place your sales dataset in the project directory
2. Update the file path in the code to point to your dataset
3. Run the Python script to generate all visualizations

## Output
The script generates five different visualizations:
1. Monthly Total Revenue Bar Plot
2. Top 5 Best-Selling Products Line Plot
3. Seasonal Sales Analysis Scatter Plot
4. Regional Sales Distribution Pie Chart
5. Historical Monthly Revenue Distribution Histogram

## Contributing
Feel free to submit issues and enhancement requests.

## License
This project is open source and available under the MIT License. 