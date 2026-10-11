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
country_revenue = sales_df.groupby("Country")["Revenue"].sum().sort_values(ascending=False)
top10 = country_revenue.head(10).sort_values(ascending=True)

fig, ax = plt.subplots(figsize=(10, 6))
top10.plot(kind="barh", ax=ax, color="steelblue", label="Filtered sales revenue")
ax.set_title("Top 10 Countries by Filtered Sales Revenue")
ax.set_xlabel("Revenue")
ax.set_ylabel("Country")
ax.legend()
ax.grid(axis="x", alpha=0.25)
fig.tight_layout()
OUTPUT_FILE = BASE_DIR / "outputs" / "figures" / "12_top_countries_bar.png"
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUTPUT_FILE, dpi=150, bbox_inches="tight")
print("Top 10 countries by filtered sales revenue:")
print(country_revenue.head(10).to_string())
print(f"\nBar chart saved to: {OUTPUT_FILE}")
plt.show()
