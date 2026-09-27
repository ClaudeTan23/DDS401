import csv
import numpy as np

# Read the CSV file
with open("../data/retail_sales_data.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Create a 2D NumPy array
sales_inventory = np.array([
    [
        float(row["Price"]),
        int(row["Quantity_Sold"]),
        int(row["Stock_Level"])
    ]
    for row in data
])

print("Sales and Inventory 2D Array:")
print(sales_inventory)

# Display array information
print("\nArray Information")
print("-------------------")
print("Shape:", sales_inventory.shape)
print("Rows:", sales_inventory.shape[0])
print("Columns:", sales_inventory.shape[1])

# Access individual columns
prices = sales_inventory[:, 0]
quantities = sales_inventory[:, 1]
stock_levels = sales_inventory[:, 2]

print("\nPrice:")
print(prices)

print("\nQuantity Sold:")
print(quantities)

print("\nStock Level:")
print(stock_levels)