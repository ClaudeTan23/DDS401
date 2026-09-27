import csv

with open("../data/retail_sales_data.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    data = list(reader)

print("Number of rows:", len(data))
print("Header:", data[0])

for row in data[1:4]:
    print(row)