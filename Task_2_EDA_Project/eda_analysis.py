
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

print("First 5 rows:")
print(df.head())
print("\nShape:", df.shape)
print("\nData types:")
print(df.dtypes)
print("\nMissing values:")
print(df.isnull().sum())
print("\nSummary statistics:")
print(df.describe())

# Sales by category
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print("\nSales by category:")
print(category_sales)

# Sales by region
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print("\nSales by region:")
print(region_sales)

# Monthly trend
df["Date"] = pd.to_datetime(df["Date"])
monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["Sales"].sum()
print("\nMonthly sales:")
print(monthly_sales)

# Visualizations
category_sales.plot(kind="bar", title="Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

monthly_sales.plot(kind="line", marker="o", title="Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# Basic insights
print("\nKEY INSIGHTS")
print(f"1. Highest-selling category: {category_sales.idxmax()}")
print(f"2. Highest-selling region: {region_sales.idxmax()}")
print(f"3. Total sales: {df['Sales'].sum():.2f}")
