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

import matplotlib.pyplot as plt

sales_df = df.loc[
    df["InvoiceDate"].notna() & df["Country"].notna()
    & df["Quantity"].notna() & df["Price"].notna()
    & (df["Quantity"] > 0) & (df["Price"] > 0)
    & (~df["IsCancellation"])
].copy()
sales_df["Revenue"] = sales_df["Quantity"] * sales_df["Price"]
monthly_revenue = sales_df.set_index("InvoiceDate")["Revenue"].resample("MS").sum()

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(monthly_revenue.index, monthly_revenue.values, marker="o", linewidth=1.8, label="Monthly revenue")
ax.set_title("Monthly Filtered Sales Revenue")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue")
ax.legend()
ax.grid(True, alpha=0.3)
fig.autofmt_xdate()
fig.tight_layout()
OUTPUT_FILE = BASE_DIR / "outputs" / "figures" / "09_monthly_revenue_line.png"
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUTPUT_FILE, dpi=150, bbox_inches="tight")
print(monthly_revenue.to_string())
print(f"\nLine plot saved to: {OUTPUT_FILE}")
plt.show()
