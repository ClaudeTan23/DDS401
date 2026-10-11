from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "data" / "online_retail_II.xlsx"

# Load and combine the worksheets
df1 = pd.read_excel(DATA_FILE, sheet_name="Year 2009-2010")
df2 = pd.read_excel(DATA_FILE, sheet_name="Year 2010-2011")
df = pd.concat([df1, df2], ignore_index=True)

# Prepare required data types
df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"], errors="coerce"
)
df["Quantity"] = pd.to_numeric(
    df["Quantity"], errors="coerce"
)
df["Price"] = pd.to_numeric(
    df["Price"], errors="coerce"
)

# Identify cancellation invoices
df["IsCancellation"] = (
    df["Invoice"].astype("string")
    .str.strip()
    .str.upper()
    .str.startswith("C", na=False)
)

# Keep records suitable for this sales summary
sales_df = df.loc[
    df["InvoiceDate"].notna()
    & df["Country"].notna()
    & df["Quantity"].notna()
    & df["Price"].notna()
    & (df["Quantity"] > 0)
    & (df["Price"] > 0)
    & (~df["IsCancellation"])
].copy()

# Calculate transaction revenue
sales_df["Revenue"] = (
    sales_df["Quantity"] * sales_df["Price"]
)

# Extract the year
sales_df["Year"] = sales_df["InvoiceDate"].dt.year

# Create a pivot table: revenue by country and year
pivot_table = pd.pivot_table(
    sales_df,
    values="Revenue",
    index="Country",
    columns="Year",
    aggfunc="sum",
    fill_value=0
)

# Add a total across years for each country
pivot_table["Total Revenue"] = pivot_table.sum(axis=1)

# Sort countries by total revenue
pivot_table = pivot_table.sort_values(
    by="Total Revenue",
    ascending=False
)

print("=== Revenue by Country and Year ===")
print(pivot_table)

print("\n=== Top 10 Countries by Revenue ===")
print(pivot_table.head(10))

# Save the pivot table
OUTPUT_FILE = BASE_DIR / "data" / "revenue_pivot_table.csv"
pivot_table.to_csv(OUTPUT_FILE)

print("\nPivot table saved to:", OUTPUT_FILE)