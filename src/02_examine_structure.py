from pathlib import Path
import pandas as pd

# Locate the Excel workbook
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "data" / "online_retail_II.xlsx"

# Load and combine both worksheets
df1 = pd.read_excel(DATA_FILE, sheet_name="Year 2009-2010")
df2 = pd.read_excel(DATA_FILE, sheet_name="Year 2010-2011")
df = pd.concat([df1, df2], ignore_index=True)

# Examine the dataset dimensions
print("=== Dataset Dimensions ===")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Display column names
print("\n=== Column Names ===")
print(df.columns.tolist())

# Display data types and non-null counts
print("\n=== Dataset Information ===")
df.info()

# Display the first and last five records
print("\n=== First Five Records ===")
print(df.head())

print("\n=== Last Five Records ===")
print(df.tail())

# Examine missing values
print("\n=== Missing Values ===")
print(df.isnull().sum())

# Examine numerical statistics
print("\n=== Numerical Summary ===")
print(df.describe())

# Count unique values in each column
print("\n=== Unique Values ===")
print(df.nunique())