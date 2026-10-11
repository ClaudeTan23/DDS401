from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "data" / "online_retail_II.xlsx"

# Load the two worksheets
df_2009_2010 = pd.read_excel(
    DATA_FILE,
    sheet_name="Year 2009-2010"
)

df_2010_2011 = pd.read_excel(
    DATA_FILE,
    sheet_name="Year 2010-2011"
)

# Add a column to identify the source worksheet
df_2009_2010["Source_Sheet"] = "2009-2010"
df_2010_2011["Source_Sheet"] = "2010-2011"

# Combine the datasets row-wise
combined_df = pd.concat(
    [df_2009_2010, df_2010_2011],
    ignore_index=True
)

# Inspect the combined dataset
print("=== Combined Dataset ===")
print("Rows:", len(combined_df))
print("Columns:", len(combined_df.columns))

print("\n=== Records by Source Worksheet ===")
print(combined_df["Source_Sheet"].value_counts())

print("\n=== Sample Combined Records ===")
print(
    combined_df[
        [
            "Invoice", "StockCode", "Description",
            "Quantity", "Price", "Country", "Source_Sheet"
        ]
    ].head()
)

# Verify the combined row count
expected_rows = len(df_2009_2010) + len(df_2010_2011)

print("\n=== Validation ===")
print("Expected rows:", expected_rows)
print("Actual rows:", len(combined_df))
print("Row count matches:", expected_rows == len(combined_df))

# Save the combined dataset
OUTPUT_FILE = BASE_DIR / "data" / "online_retail_combined.csv"
combined_df.to_csv(OUTPUT_FILE, index=False)

print("\nCombined dataset saved to:", OUTPUT_FILE)