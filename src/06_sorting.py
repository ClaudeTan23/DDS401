import csv
import numpy as np

# Read the CSV file
with open("../data/retail_sales_data.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Create a NumPy array for quantity sold
quantities = np.array([
    int(row["Quantity_Sold"])
    for row in data
])

# Sort indices by quantity sold from highest to lowest
sorted_indices = np.argsort(quantities)[::-1]

# Display sorted results
print("Products Sorted by Quantity Sold")
print("---------------------------------")

for index in sorted_indices:
    product_id = data[index]["Product_ID"]
    category = data[index]["Category"]
    quantity = quantities[index]

    print(f"{product_id} - {category} - {quantity} units")