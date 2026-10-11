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
scatter_df = sales_df[["Quantity", "Price"]]
if len(scatter_df) > 10000:
    scatter_df = scatter_df.sample(n=10000, random_state=42)
country_revenue = sales_df.groupby("Country")["Revenue"].sum().sort_values(ascending=False).head(10).sort_values()

fig, axes = plt.subplots(2, 2, figsize=(15, 10))
axes[0, 0].plot(monthly_revenue.index, monthly_revenue.values, marker="o", label="Monthly revenue")
axes[0, 0].set_title("Monthly Sales Revenue")
axes[0, 0].set_xlabel("Month")
axes[0, 0].set_ylabel("Revenue")
axes[0, 0].legend()
axes[0, 0].tick_params(axis="x", rotation=35)
axes[0, 1].scatter(scatter_df["Quantity"], scatter_df["Price"], alpha=0.3, s=12, label="Transactions")
axes[0, 1].set_title("Quantity versus Unit Price")
axes[0, 1].set_xlabel("Quantity")
axes[0, 1].set_ylabel("Unit price")
axes[0, 1].legend()
axes[1, 0].hist(sales_df["Price"], bins=50, edgecolor="black", label="Transactions")
axes[1, 0].set_title("Unit Price Distribution")
axes[1, 0].set_xlabel("Unit price")
axes[1, 0].set_ylabel("Frequency")
axes[1, 0].legend()
country_revenue.plot(kind="barh", ax=axes[1, 1], label="Revenue")
axes[1, 1].set_title("Top 10 Countries by Revenue")
axes[1, 1].set_xlabel("Revenue")
axes[1, 1].set_ylabel("Country")
axes[1, 1].legend()
fig.suptitle("Online Retail II: Exploratory Visualisations", fontsize=15)
fig.tight_layout()
OUTPUT_FILE = BASE_DIR / "outputs" / "figures" / "13_combined_visualizations.png"
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUTPUT_FILE, dpi=150, bbox_inches="tight")
print(f"Combined visualisation saved to: {OUTPUT_FILE}")
plt.show()
