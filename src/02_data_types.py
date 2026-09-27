import csv

# Read the CSV file
with open("../data/retail_sales_data.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Select the first product
product = data[0]

# Convert values to appropriate Python data types
product_id = product["Product_ID"]
category = product["Category"]
price = float(product["Price"])
quantity_sold = int(product["Quantity_Sold"])
stock_level = int(product["Stock_Level"])
discount_percent = float(product["Discount_Percent"])

# Display the variables and their values
print("Product Information")
print("-------------------")
print("Product ID:", product_id)
print("Category:", category)
print("Price:", price)
print("Quantity Sold:", quantity_sold)
print("Stock Level:", stock_level)
print("Discount:", discount_percent)

# Display the data types
print("\nData Types")
print("-------------------")
print("Product ID:", type(product_id).__name__)
print("Category:", type(category).__name__)
print("Price:", type(price).__name__)
print("Quantity Sold:", type(quantity_sold).__name__)
print("Stock Level:", type(stock_level).__name__)
print("Discount:", type(discount_percent).__name__)