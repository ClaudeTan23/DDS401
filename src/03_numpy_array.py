import csv
import numpy as np

# Read the CSV file
with open("../data/retail_sales_data.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Extract quantity sold from each product
quantity_sold = np.array(
    [int(row["Quantity_Sold"]) for row in data]
)

# Display the NumPy array
print("Quantity Sold:")
print(quantity_sold)

# Display basic array information
print("\nArray Information")
print("-------------------")
print("Number of products:", quantity_sold.size)
print("Array shape:", quantity_sold.shape)
print("Data type:", quantity_sold.dtype)