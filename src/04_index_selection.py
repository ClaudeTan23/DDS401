from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "data" / "online_retail_II.xlsx"

# Load and combine the worksheets
df1 = pd.read_excel(DATA_FILE, sheet_name="Year 2009-2010")
df2 = pd.read_excel(DATA_FILE, sheet_name="Year 2010-2011")
df = pd.concat([df1, df2], ignore_index=True)

# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"], errors="coerce"
)

# 1. Select individual columns
print("=== Selected Columns ===")
print(df[["Invoice", "Description", "Quantity", "Price"]].head())

# 2. Select rows by position using iloc
print("\n=== First Five Rows Using iloc ===")
print(df.iloc[0:5])

# 3. Select rows and columns by labels using loc
print("\n=== Selected Rows and Columns Using loc ===")
print(df.loc[0:4, ["Invoice", "Country", "Quantity", "Price"]])

# 4. Select transactions from the United Kingdom
uk_transactions = df.loc[df["Country"] == "United Kingdom"]

print("\n=== United Kingdom Transactions ===")
print(uk_transactions.head())
print("Number of UK records:", len(uk_transactions))

# 5. Select records with positive quantities and prices
valid_values = df.loc[
    (df["Quantity"] > 0) &
    (df["Price"] > 0),
    ["Invoice", "Description", "Quantity", "Price"]
]

print("\n=== Records With Positive Quantity and Price ===")
print(valid_values.head())
print("Number of selected records:", len(valid_values))

# 6. Select transactions from December 2010
december_2010 = df.loc[
    df["InvoiceDate"].between(
        "2010-12-01", "2010-12-31 23:59:59"
    )
]

print("\n=== December 2010 Transactions ===")
print(december_2010.head())
print("Number of December 2010 records:", len(december_2010))