import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.gridspec import GridSpec
import numpy as np
from pathlib import Path

# ==========================================================
# Executive Sales Performance Dashboard
# Retail Analytics & Business Insights
# ==========================================================

# Locate project root
BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_DIR = BASE_DIR / "Dataset"
SCREENSHOT_DIR = BASE_DIR / "Screenshots"

customers = pd.read_csv(DATASET_DIR / "customers.csv")
products = pd.read_csv(DATASET_DIR / "products.csv")
stores = pd.read_csv(DATASET_DIR / "stores.csv")
orders = pd.read_csv(DATASET_DIR / "orders.csv")
order_details = pd.read_csv(DATASET_DIR / "order_details.csv")

orders["order_date"] = pd.to_datetime(orders["order_date"])

sales = (
    order_details
    .merge(products, on="product_id")
    .merge(orders, on="order_id")
    .merge(customers, on="customer_id")
    .merge(stores, on="store_id")
)
sales["Revenue"] = (
    sales["price"]
    * sales["quantity"]
    * (1 - sales["discount"] / 100)
)
print("=" * 60)
print("MASTER DATASET")
print("=" * 60)

print(sales.head())

print("\nShape :", sales.shape)

# ==========================================================
# Executive KPI Calculations
# ==========================================================

total_revenue = sales["Revenue"].sum()

total_orders = orders["order_id"].nunique()

total_customers = customers["customer_id"].nunique()

total_products = products["product_id"].nunique()

total_stores = stores["store_id"].nunique()

total_quantity = sales["quantity"].sum()

average_order_value = total_revenue / total_orders

print("\n")
print("=" * 60)
print("EXECUTIVE KPIs")
print("=" * 60)

print(f"Total Revenue        : ₹{total_revenue:,.2f}")
print(f"Total Orders         : {total_orders:,}")
print(f"Total Customers      : {total_customers:,}")
print(f"Total Products       : {total_products}")
print(f"Total Stores         : {total_stores}")
print(f"Products Sold        : {total_quantity:,}")
print(f"Average Order Value  : ₹{average_order_value:,.2f}")

# ==========================================================
# Revenue Validation
# ==========================================================

print("\n")
print("=" * 60)
print("REVENUE VALIDATION")
print("=" * 60)

print(f"Minimum Product Price : ₹{products['price'].min():,.2f}")
print(f"Maximum Product Price : ₹{products['price'].max():,.2f}")

print(f"Average Product Price : ₹{products['price'].mean():,.2f}")

print(f"Minimum Quantity      : {sales['quantity'].min()}")

print(f"Maximum Quantity      : {sales['quantity'].max()}")

print(f"Average Quantity      : {sales['quantity'].mean():.2f}")

print(f"Average Discount (%)  : {sales['discount'].mean():.2f}")
# ==========================================================
# Number Formatting
# ==========================================================

def format_number(num):

    if num >= 1_000_000_000:
        return f"₹{num/1_000_000_000:.2f} B"

    elif num >= 1_000_000:
        return f"₹{num/1_000_000:.2f} M"

    elif num >= 1000:
        return f"{num/1000:.1f} K"

    else:
        return str(num)
    
# ==========================================================
# Dashboard Metrics
# ==========================================================

# Revenue by Category
category_revenue = (
    sales.groupby("category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

# Revenue by Store
store_revenue = (
    sales.groupby("store_name")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

# Top 10 Products
top_products = (
    sales.groupby("product_name")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# Monthly Revenue
monthly_revenue = (
    sales.groupby(sales["order_date"].dt.to_period("M"))["Revenue"]
    .sum()
)

monthly_revenue.index = monthly_revenue.index.astype(str)


# Payment Methods
payment_methods = (
    orders["payment_method"]
    .value_counts()
)

# Order Status
order_status = (
    orders["order_status"]
    .value_counts()
)
print("\n")
print("="*60)
print("BUSINESS INSIGHTS")
print("="*60)

print("\nTop Category")
print(category_revenue.head())

print("\nTop Stores")
print(store_revenue.head())

print("\nTop Products")
print(top_products.head())

print("\nPayment Methods")
print(payment_methods)

print("\nOrder Status")
print(order_status)

# ==========================================================
# Create Dashboard Canvas
# ==========================================================

plt.style.use("default")

fig = plt.figure(figsize=(20, 12), facecolor="#0B1220")

gs = GridSpec(
    28,
    24,
    figure=fig,
    left=0.04,
    right=0.96,
    top=0.95,
    bottom=0.05,
    wspace=0.70,
    hspace=1.60
)
# ==========================================================
# Dashboard Header
# ==========================================================

header = fig.add_subplot(gs[0:2, :])

header.set_facecolor("#111827")

header.set_xticks([])
header.set_yticks([])

for spine in header.spines.values():
    spine.set_visible(False)

header.text(
    0.5,
    0.72,
    "EXECUTIVE SALES PERFORMANCE DASHBOARD",
    ha="center",
    va="center",
    fontsize=26,
    color="white",
    fontweight="bold"
)


header.text(
    0.5,
    0.36,
    "Retail Analytics & Business Insights",
    ha="center",
    va="center",
    fontsize=13,
    color="#9CA3AF"
)

header.text(
    0.99,
    0.85,
    "SQL • Python • Pandas • Matplotlib • MySQL",
    ha="right",
    va="center",
    fontsize=10,
    color="#60A5FA"
)
# ==========================================================
# KPI Card Function
# ==========================================================

def draw_card(ax, title, value, color):

    ax.set_facecolor("#162033")

    ax.set_xticks([])
    ax.set_yticks([])

    for spine in ax.spines.values():
        spine.set_visible(False)

    # Left Color Strip
    ax.add_patch(
        patches.Rectangle(
            (0, 0),
            0.04,
            1,
            transform=ax.transAxes,
            color=color
        )
    )

    # Card Title
    ax.text(
        0.08,
        0.72,
        title.upper(),
        fontsize=11,
        fontweight="bold",
        color="#CBD5E1",
        transform=ax.transAxes
    )

    # Card Value
    ax.text(
        0.08,
        0.28,
        value,
        fontsize=22,
        fontweight="bold",
        color="white",
        transform=ax.transAxes
    )


# ==========================================================
# KPI Cards
# ==========================================================

card1 = fig.add_subplot(gs[2:5, 0:4])
card2 = fig.add_subplot(gs[2:5, 4:8])
card3 = fig.add_subplot(gs[2:5, 8:12])
card4 = fig.add_subplot(gs[2:5, 12:16])
card5 = fig.add_subplot(gs[2:5, 16:20])
card6 = fig.add_subplot(gs[2:5, 20:24])


draw_card(
    card1,
    "Revenue",
    format_number(total_revenue),
    "#3B82F6"
)

draw_card(
    card2,
    "Orders",
    format_number(total_orders),
    "#06B6D4"
)

draw_card(
    card3,
    "Customers",
    format_number(total_customers),
    "#8B5CF6"
)

draw_card(
    card4,
    "Products",
    str(total_products),
    "#22C55E"
)

draw_card(
    card5,
    "Stores",
    str(total_stores),
    "#F59E0B"
)

draw_card(
    card6,
    "Avg Order",
    format_number(average_order_value),
    "#EC4899"
)
# ==========================================================
# Monthly Revenue Chart
# ==========================================================

monthly_chart = fig.add_subplot(gs[5:12, 0:12])

monthly_chart.set_facecolor("#162033")

months = monthly_revenue.index.astype(str)

monthly_chart.plot(
    months,
    monthly_revenue.values,
    color="#3B82F6",
    linewidth=3,
    marker="o",
    markersize=7
)

monthly_chart.fill_between(
    months,
    monthly_revenue.values,
    color="#3B82F6",
    alpha=0.20
)

monthly_chart.set_title(
    "Monthly Revenue Trend",
    fontsize=15,
    color="white",
    fontweight="bold",
    pad=15
)

monthly_chart.tick_params(axis='x', colors='white', rotation=45)
monthly_chart.tick_params(axis='y', colors='white')

monthly_chart.grid(
    alpha=0.25,
    linestyle="--"
)

for spine in monthly_chart.spines.values():
    spine.set_color("#2A3B55")
   
   # ==========================================================
# Revenue by Category (Donut Chart)
# ==========================================================

category_chart = fig.add_subplot(gs[5:12, 13:24])

category_chart.set_facecolor("#162033")

colors = [
    "#3B82F6",
    "#8B5CF6",
    "#06B6D4",
    "#22C55E",
    "#F59E0B",
    "#EC4899"
]

wedges, texts, autotexts = category_chart.pie(
    category_revenue.values,
    labels=category_revenue.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=colors,
    wedgeprops=dict(width=0.45, edgecolor="#162033"),
    textprops=dict(color="white", fontsize=9)
)

category_chart.set_title(
    "Revenue by Category",
    fontsize=15,
    color="white",
    fontweight="bold",
    pad=15
)
# ==========================================================
# Revenue by Store
# ==========================================================

store_chart = fig.add_subplot(gs[13:21, 0:12])

store_chart.set_facecolor("#162033")

top_store = store_revenue.head(8)

store_chart.barh(
    top_store.index,
    top_store.values,
    color="#3B82F6"
)

for i, v in enumerate(top_store.values):
    store_chart.text(
     v - 8000000,
        i,
        f"{v/1_000_000:.1f}M",
        va="center",
        fontsize=8,
        color="#E5E7EB"
    )

store_chart.set_title(
    "Top Stores by Revenue",
    fontsize=15,
    color="white",
    fontweight="bold",
    pad=15
)

store_chart.tick_params(axis="x", colors="white")
store_chart.tick_params(axis="y", colors="white")

store_chart.grid(
    axis="x",
    linestyle="--",
    alpha=0.25
)

for spine in store_chart.spines.values():
    spine.set_color("#2A3B55")
    
    # ==========================================================
# Top Products
# ==========================================================

product_chart = fig.add_subplot(gs[13:21, 13:24])

product_chart.set_facecolor("#162033")

product_chart.barh(
    top_products.index[::-1],
    top_products.values[::-1],
    color="#22C55E"
)

for i, v in enumerate(top_products.values[::-1]):
    product_chart.text(
        v + 1000000,
        i,
        f"{v/1_000_000:.1f}M",
        va="center",
        fontsize=8,
        color="white"
    )

product_chart.set_title(
    "Top 10 Products by Revenue",
    fontsize=15,
    color="white",
    fontweight="bold",
    pad=15
)

product_chart.tick_params(axis="x", colors="white")
product_chart.tick_params(axis="y", colors="white")

product_chart.grid(
    axis="x",
    linestyle="--",
    alpha=0.25
)

for spine in product_chart.spines.values():
    spine.set_color("#2A3B55")
 
 # ==========================================================
# Payment Method Distribution
# ==========================================================

payment_chart = fig.add_subplot(gs[22:28, 0:7])

payment_chart.set_facecolor("#162033")

payment_colors = [
    "#3B82F6",
    "#06B6D4",
    "#8B5CF6",
    "#22C55E",
    "#F59E0B"
]

payment_chart.pie(
    payment_methods.values,
    labels=payment_methods.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=payment_colors,
    wedgeprops=dict(width=0.45, edgecolor="#162033"),
    textprops=dict(color="white", fontsize=8)
)

payment_chart.set_title(
    "Payment Methods",
    fontsize=14,
    color="white",
    fontweight="bold"
)
 
 # ==========================================================
# Order Status
# ==========================================================

status_chart = fig.add_subplot(gs[22:28, 8:15])

status_chart.set_facecolor("#162033")

status_colors = [
    "#22C55E",
    "#3B82F6",
    "#F59E0B",
    "#EF4444",
    "#8B5CF6"
]

status_chart.pie(
    order_status.values,
    labels=order_status.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=status_colors,
    wedgeprops=dict(width=0.45, edgecolor="#162033"),
    textprops=dict(color="white", fontsize=8)
)

status_chart.set_title(
    "Order Status",
    fontsize=14,
    color="white",
    fontweight="bold"
)

# ==========================================================
# Executive Insights
# ==========================================================

insights = fig.add_subplot(gs[22:28, 17:24])

insights.set_facecolor("#162033")

insights.set_xticks([])
insights.set_yticks([])

for spine in insights.spines.values():
    spine.set_visible(False)

best_category = category_revenue.idxmax()
best_store = store_revenue.idxmax()
best_product = top_products.idxmax()
best_payment = payment_methods.idxmax()

insights.text(
    0.05,
    0.92,
    "EXECUTIVE INSIGHTS",
    fontsize=16,
    fontweight="bold",
    color="white"
)

insights.text(
    0.05,
    0.74,
    f"🏆 Best Category : {best_category}",
    fontsize=12,
    color="#CBD5E1"
)

insights.text(
    0.05,
    0.60,
    f"🏪 Best Store : {best_store}",
    fontsize=11,
    color="#CBD5E1"
)

insights.text(
    0.05,
    0.46,
    f"📦 Best Product : {best_product}",
    fontsize=11,
    color="#CBD5E1"
)

insights.text(
    0.05,
    0.32,
    f"💳 Top Payment : {best_payment}",
    fontsize=11,
    color="#CBD5E1"
)

insights.text(
    0.05,
    0.18,
    f"💰 Revenue : ₹{total_revenue/1_000_000_000:.2f} Billion",
    fontsize=11,
    color="#CBD5E1"
)
 
fig.text(
    0.5,
    0.015,
    "Created by Shreya Sanjay Kumbharkar | Python • Pandas • Matplotlib • MySQL",
    ha="center",
    fontsize=10,
    color="#94A3B8"
)
 
plt.savefig(
    SCREENSHOT_DIR / "retail_sales_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nDashboard layout created successfully!")