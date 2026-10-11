from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "data" / "online_retail_II.xlsx"

# Load and combine the worksheets
df1 = pd.read_excel(DATA_FILE, sheet_name="Year 2009-2010")
df2 = pd.read_excel(DATA_FILE, sheet_name="Year 2010-2011")
df = pd.concat([df1, df2], ignore_index=True)

print("Original dataset shape:", df.shape)

# Standardise column names
df.columns = df.columns.str.strip()

# Standardise text fields
for column in ["Description", "Country", "StockCode"]:
    df[column] = df[column].astype("string").str.strip()

# Convert columns to appropriate data types
df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"], errors="coerce"
)
df["Quantity"] = pd.to_numeric(
    df["Quantity"], errors="coerce"
)
df["Price"] = pd.to_numeric(
    df["Price"], errors="coerce"
)

# Inspect missing values before handling them
print("\n=== Missing Values Before Cleaning ===")
print(df.isnull().sum())

# Count exact duplicate rows before removing them
print("\nExact duplicate rows:", df.duplicated().sum())

# Remove exact duplicate records
df = df.drop_duplicates().copy()

# Replace missing descriptions with a clear label
df["Description"] = df["Description"].fillna(
    "Unknown description"
)

# Keep missing Customer IDs because they may still be
# useful for analysing transactions not linked to a customer.
# Do not automatically replace missing IDs with invented IDs.

# Identify cancellation invoices
df["IsCancellation"] = (
    df["Invoice"].astype("string")
    .str.strip()
    .str.upper()
    .str.startswith("C", na=False)
)

# Identify records with invalid or incomplete key fields
invalid_dates = df["InvoiceDate"].isna()
invalid_quantity = df["Quantity"].isna()
invalid_price = df["Price"].isna()

print("\n=== Data Quality Checks ===")
print("Invalid dates:", invalid_dates.sum())
print("Missing quantities:", invalid_quantity.sum())
print("Missing prices:", invalid_price.sum())
print("Cancellation invoices:", df["IsCancellation"].sum())
print("Non-positive quantities:", (df["Quantity"] <= 0).sum())
print("Negative prices:", (df["Price"] < 0).sum())

# Save the cleaned dataset for later scripts
OUTPUT_FILE = BASE_DIR / "data" / "online_retail_cleaned.csv"
df.to_csv(OUTPUT_FILE, index=False)

print("\nCleaned dataset shape:", df.shape)
print("Cleaned dataset saved to:", OUTPUT_FILE)
print("\nRemaining missing values:")
print(df.isnull().sum())