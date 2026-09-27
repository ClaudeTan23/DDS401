import csv
import numpy as np

# Read the CSV file
with open("../data/retail_sales_data.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Create NumPy arrays
prices = np.array([
    float(row["Price"])
    for row in data
])

quantities = np.array([
    int(row["Quantity_Sold"])
    for row in data
])

stock_levels = np.array([
    int(row["Stock_Level"])
    for row in data
])

# Calculate revenue for each product
revenue = np.multiply(prices, quantities)

# Calculate total revenue
total_revenue = np.sum(revenue)

# Calculate average quantity sold
average_quantity = np.mean(quantities)

# Find highest and lowest stock levels
highest_stock = np.max(stock_levels)
lowest_stock = np.min(stock_levels)

# Display results
print("Revenue for Each Product:")
print(revenue)

print("\nTotal Revenue: RM", total_revenue)
print("Average Quantity Sold:", average_quantity)

print("\nStock Level Analysis")
print("-------------------")
print("Highest Stock Level:", highest_stock)
print("Lowest Stock Level:", lowest_stock)