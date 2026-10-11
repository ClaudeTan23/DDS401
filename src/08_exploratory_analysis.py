from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "data" / "online_retail_II.xlsx"

if not DATA_FILE.exists():
    raise FileNotFoundError(
        f"Dataset not found: {DATA_FILE}\n"
        "Place online_retail_II.xlsx inside the project's data folder."
    )

# Load and combine both worksheets
df1 = pd.read_excel(DATA_FILE, sheet_name="Year 2009-2010")
df2 = pd.read_excel(DATA_FILE, sheet_name="Year 2010-2011")
df = pd.concat([df1, df2], ignore_index=True)

# Prepare data types used by this analysis
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df["Invoice"] = df["Invoice"].astype("string").str.strip()
df["IsCancellation"] = df["Invoice"].str.upper().str.startswith("C", na=False)

# Create a positive-sales dataset for consistent sales analysis
sales_df = df.loc[
    df["InvoiceDate"].notna()
    & df["Country"].notna()
    & df["Quantity"].notna()
    & df["Price"].notna()
    & (df["Quantity"] > 0)
    & (df["Price"] > 0)
    & (~df["IsCancellation"])
].copy()
sales_df["Revenue"] = sales_df["Quantity"] * sales_df["Price"]
sales_df["YearMonth"] = sales_df["InvoiceDate"].dt.to_period("M").astype(str)

print("=== Dataset overview ===")
print(f"Combined rows and columns: {df.shape}")
print("\n=== Column data types and non-null counts ===")
df.info()
print("\n=== Missing values by column ===")
print(df.isna().sum().sort_values(ascending=False))
print("\n=== Numerical summary ===")
print(df[["Quantity", "Price"]].describe())
print("\n=== Sales summary ===")
print(f"Rows retained for positive-sales analysis: {len(sales_df):,}")
print(f"Total filtered sales revenue: {sales_df['Revenue'].sum():,.2f}")
print("\n=== Monthly revenue (first 12 periods) ===")
print(sales_df.groupby("YearMonth")["Revenue"].sum().head(12).to_string())
