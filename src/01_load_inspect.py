
from pathlib import Path
import pandas as pd

# --------------------------------------------------
# 1. Define the dataset location
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "data" / "online_retail_II.xlsx"

# --------------------------------------------------
# 2. Import both worksheets
# --------------------------------------------------

sheet_2009_2010 = pd.read_excel(
    DATA_FILE,
    sheet_name="Year 2009-2010"
)

sheet_2010_2011 = pd.read_excel(
    DATA_FILE,
    sheet_name="Year 2010-2011"
)

print("Dataset imported successfully.")
print(f"2009-2010 records: {len(sheet_2009_2010):,}")
print(f"2010-2011 records: {len(sheet_2010_2011):,}")

# --------------------------------------------------
# 3. Combine both worksheets
# --------------------------------------------------

df = pd.concat(
    [
        sheet_2009_2010,
        sheet_2010_2011
    ],
    ignore_index=True
)

print("\nCombined dataset created.")

# --------------------------------------------------
# 4. Inspect the dataset
# --------------------------------------------------

print("\n--- First 5 Records ---")
print(df.head())

print("\n--- Last 5 Records ---")
print(df.tail())

print("\n--- Dataset Dimensions ---")
print(f"Rows: {df.shape[0]:,}")
print(f"Columns: {df.shape[1]}")

print("\n--- Column Names ---")
print(df.columns.tolist())

print("\n--- Data Types and Non-Null Counts ---")
df.info()

print("\n--- Numerical Summary Statistics ---")
print(df.describe())

print("\n--- DataFrame Memory Usage ---")
print(f"{df.memory_usage(deep=True).sum() / (1024 ** 2):.2f} MB")