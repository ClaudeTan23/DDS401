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
# Sample large datasets for readability; random_state makes the sample reproducible.
plot_df = sales_df[["Quantity", "Price"]]
if len(plot_df) > 10000:
    plot_df = plot_df.sample(n=10000, random_state=42)

fig, ax = plt.subplots(figsize=(9, 6))
ax.scatter(plot_df["Quantity"], plot_df["Price"], alpha=0.35, s=18, label="Transactions")
ax.set_title("Transaction Quantity versus Unit Price")
ax.set_xlabel("Quantity")
ax.set_ylabel("Unit price")
ax.legend()
ax.grid(True, alpha=0.25)
fig.tight_layout()
OUTPUT_FILE = BASE_DIR / "outputs" / "figures" / "10_quantity_price_scatter.png"
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUTPUT_FILE, dpi=150, bbox_inches="tight")
print(f"Rows displayed in scatter plot: {len(plot_df):,}")
print("A reproducible random sample is used when there are more than 10,000 eligible transactions.")
print(f"Scatter plot saved to: {OUTPUT_FILE}")
plt.show()
