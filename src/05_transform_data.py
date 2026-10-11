from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "data" / "online_retail_II.xlsx"

# Load and combine the worksheets
df1 = pd.read_excel(DATA_FILE, sheet_name="Year 2009-2010")
df2 = pd.read_excel(DATA_FILE, sheet_name="Year 2010-2011")
df = pd.concat([df1, df2], ignore_index=True)

# Convert data types
df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"], errors="coerce"
)
df["Quantity"] = pd.to_numeric(
    df["Quantity"], errors="coerce"
)
df["Price"] = pd.to_numeric(
    df["Price"], errors="coerce"
)

# Create a revenue column
df["Revenue"] = df["Quantity"] * df["Price"]

# Extract year and month for time-based analysis
df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.month
df["YearMonth"] = df["InvoiceDate"].dt.to_period("M").astype("string")

# Identify cancellation invoices
df["IsCancellation"] = (
    df["Invoice"].astype("string")
    .str.strip()
    .str.upper()
    .str.startswith("C", na=False)
)

# Create a filtered dataset for positive-quantity sales
# with valid dates and positive prices.
sales_df = df.loc[
    df["InvoiceDate"].notna()
    & df["Quantity"].notna()
    & df["Price"].notna()
    & (df["Quantity"] > 0)
    & (df["Price"] > 0)
    & (~df["IsCancellation"])
].copy()

print("=== Transformed Data ===")
print(
    sales_df[
        [
            "Invoice", "InvoiceDate", "Quantity",
            "Price", "Revenue", "Year", "Month", "YearMonth"
        ]
    ].head()
)

print("\nNumber of records before filtering:", len(df))
print("Number of sales records after filtering:", len(sales_df))
print("Total revenue in filtered records:", sales_df["Revenue"].sum())

# Save the transformed sales data
OUTPUT_FILE = BASE_DIR / "data" / "online_retail_sales.csv"
sales_df.to_csv(OUTPUT_FILE, index=False)

print("\nTransformed data saved to:", OUTPUT_FILE)