import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from numpy.ma.extras import unique

a=pd.read_excel("C:\\Users\\anand sai reddy\\Downloads\\sales_dataset.xlsx")
print(a)
print(a.head())
print(a.tail())
print(a.info())
print(a.describe())
print(a.columns)
print(a.isnull().sum())

# Preprocess the data
a['Date'] = pd.to_datetime(a['Date'])
a['Total Revenue'] = pd.to_numeric(a['Total Revenue'], errors='coerce')
a['Month'] = a['Date'].dt.to_period('M')
a['Quarter'] = a['Date'].dt.to_period('Q')

# 1. Track Monthly Sales Growth - Barplot
monthly_revenue = a.groupby('Month')['Total Revenue'].sum().sort_index()
plt.figure(figsize=(12, 6))
monthly_revenue.plot(kind='bar', color='mediumseagreen')
plt.title('Monthly Total Revenue')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# 2. Identify Best-Selling Products - Lineplot
top_products = a.groupby('Product Name')['Total Revenue'].sum().sort_values(ascending=False).head(5)
plt.figure(figsize=(10, 5))
sns.lineplot(x=top_products.index, y=top_products.values, marker='o', color='darkorange')
plt.title('Top 5 Best-Selling Products by Total Revenue')
plt.xlabel('Product Name')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.show()

# 3. Seasonal Sales Analysis - Scatterplot
monthly_sales = a.groupby(a['Date'].dt.month)['Total Revenue'].sum()
plt.figure(figsize=(10, 6))
sns.scatterplot(x=monthly_sales.index, y=monthly_sales.values, s=100, color='royalblue')
plt.title('Seasonal Sales Analysis (Monthly Total Revenue)')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.xticks(np.arange(1, 13))
plt.grid(True)
plt.show()

# 4. Evaluate Regional Performance - Pie Chart (Latest Quarter)
latest_quarter = a['Quarter'].max()
regional_data = a[a['Quarter'] == latest_quarter].groupby('Customer Region')['Total Revenue'].sum()
plt.figure(figsize=(8, 8))
plt.pie(regional_data, labels=regional_data.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title(f'Regional Sales Distribution - {latest_quarter}')
plt.show()

# 5. Sales Forecasting Insight - Histplot
monthly_revenue_series = a.set_index('Date').resample('ME')['Total Revenue'].sum()
plt.figure(figsize=(10, 6))
sns.histplot(monthly_revenue_series, bins=12, kde=True, color='slateblue')
plt.title('Historical Monthly Revenue Distribution')
plt.xlabel('Monthly Revenue')
plt.ylabel('Frequency')
plt.show()