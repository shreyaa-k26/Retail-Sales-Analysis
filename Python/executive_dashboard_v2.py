import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.gridspec import GridSpec
from matplotlib.ticker import FuncFormatter
from pathlib import Path
import numpy as np

# ==========================================================
# Executive Sales Performance Dashboard V2
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_DIR = BASE_DIR / "Dataset"
SCREENSHOT_DIR = BASE_DIR / "Screenshots"

# ----------------------------------------------------------
# Load Datasets
# ----------------------------------------------------------

customers = pd.read_csv(DATASET_DIR / "customers.csv")
products = pd.read_csv(DATASET_DIR / "products.csv")
stores = pd.read_csv(DATASET_DIR / "stores.csv")
orders = pd.read_csv(DATASET_DIR / "orders.csv")
order_details = pd.read_csv(DATASET_DIR / "order_details.csv")

orders["order_date"] = pd.to_datetime(orders["order_date"])

# ----------------------------------------------------------
# Create Master Dataset
# ----------------------------------------------------------

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

# ----------------------------------------------------------
# KPI Calculations
# ----------------------------------------------------------

total_revenue = sales["Revenue"].sum()

total_orders = orders["order_id"].nunique()

total_customers = customers["customer_id"].nunique()

total_products = products["product_id"].nunique()

total_stores = stores["store_id"].nunique()

products_sold = sales["quantity"].sum()

average_order = total_revenue / total_orders

# ----------------------------------------------------------
# Business Analysis
# ----------------------------------------------------------

category_revenue = (
    sales.groupby("category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

store_revenue = (
    sales.groupby("store_name")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

state_revenue = (
    sales.groupby("state_y")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(8)
)

top_products = (
    sales.groupby("product_name")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

payment_methods = (
    orders["payment_method"]
    .value_counts()
)

order_status = (
    orders["order_status"]
    .value_counts()
)

monthly_revenue = (
    sales.groupby(
        sales["order_date"].dt.month_name().str[:3]
    )["Revenue"]
    .sum()
)

months = [
    "Jan","Feb","Mar","Apr","May","Jun",
    "Jul","Aug","Sep","Oct","Nov","Dec"
]

monthly_revenue = monthly_revenue.reindex(months)

# ----------------------------------------------------------
# Executive Insights
# ----------------------------------------------------------

best_category = category_revenue.idxmax()

best_store = store_revenue.idxmax()

best_product = top_products.idxmax()

best_payment = payment_methods.idxmax()

delivery_rate = (
    order_status.get("Delivered", 0)
    / total_orders
) * 100

# ----------------------------------------------------------
# Number Formatter
# ----------------------------------------------------------

def money(x):
    if x >= 1_000_000_000:
        return f"₹{x/1_000_000_000:.2f}B"

    if x >= 1_000_000:
        return f"₹{x/1_000_000:.1f}M"

    if x >= 1000:
        return f"₹{x/1000:.1f}K"

    return f"₹{x:.0f}"

print("\nDashboard data prepared successfully.")

# ==========================================================
# CREATE DASHBOARD CANVAS
# ==========================================================

plt.style.use("default")

fig = plt.figure(figsize=(22, 14), facecolor="#0B1220")

gs = GridSpec(
    30,
    24,
    figure=fig,
    left=0.04,
    right=0.97,
    top=0.94,
    bottom=0.04,
    wspace=1.2,
    hspace=2.0
)

# ==========================================================
# HEADER
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
    0.20,
    "Retail Analytics & Business Insights",
    ha="center",
    va="center",
    fontsize=13,
    color="#94A3B8"
)

header.text(
    0.99,
    0.84,
    "SQL • Python • Pandas • Matplotlib • MySQL",
    ha="right",
    fontsize=10,
    color="#60A5FA"
)

# ==========================================================
# KPI CARD FUNCTION
# ==========================================================

def draw_card(ax, title, value, color):

    ax.set_facecolor("#111827")

    ax.set_xticks([])
    ax.set_yticks([])

    for s in ax.spines.values():
        s.set_visible(False)

    # ------------------------------------------------------
    # Main Card
    # ------------------------------------------------------

    card = patches.FancyBboxPatch(
        (0.015, 0.04),
        0.97,
        0.92,
        boxstyle="round,pad=0.02,rounding_size=0.05",
        linewidth=1.5,
        edgecolor="#263449",
        facecolor="#162033",
        transform=ax.transAxes
    )

    ax.add_patch(card)

    # ------------------------------------------------------
    # Accent Line
    # ------------------------------------------------------

    accent = patches.FancyBboxPatch(
        (0.015, 0.04),
        0.018,
        0.92,
        boxstyle="round,pad=0.002,rounding_size=0.01",
        linewidth=0,
        facecolor=color,
        transform=ax.transAxes
    )

    ax.add_patch(accent)

    # ------------------------------------------------------
    # Title
    # ------------------------------------------------------

    ax.text(
        0.10,
        0.68,
        title.upper(),
        ha="left",
        va="center",
        fontsize=9,
        color="#94A3B8",
        fontweight="bold",
        transform=ax.transAxes
    )

    # ------------------------------------------------------
    # Value
    # ------------------------------------------------------

    ax.text(
        0.10,
        0.36,
        value,
        ha="left",
        va="center",
        fontsize=18,
        color="white",
        fontweight="bold",
        transform=ax.transAxes
    )


# ==========================================================
# KPI CARDS
# ==========================================================

card1 = fig.add_subplot(gs[2:5, 0:4])
draw_card(card1, "Revenue", money(total_revenue), "#3B82F6")

card2 = fig.add_subplot(gs[2:5, 4:8])
draw_card(card2, "Orders", f"{total_orders:,}", "#8B5CF6")

card3 = fig.add_subplot(gs[2:5, 8:12])
draw_card(card3, "Customers", f"{total_customers:,}", "#22C55E")

card4 = fig.add_subplot(gs[2:5, 12:16])
draw_card(card4, "Products", f"{total_products}", "#F59E0B")

card5 = fig.add_subplot(gs[2:5, 16:20])
draw_card(card5, "Stores", f"{total_stores}", "#EF4444")

card6 = fig.add_subplot(gs[2:5, 20:24])
draw_card(card6, "Avg Order", money(average_order), "#EC4899")

# ==========================================================
# MONTHLY REVENUE TREND
# ==========================================================

monthly_chart = fig.add_subplot(gs[6:12, 0:12])

monthly_chart.set_facecolor("#162033")

for spine in monthly_chart.spines.values():
    spine.set_color("#2A3B55")

monthly_chart.set_title(
    "Monthly Revenue Trend",
    fontsize=15,
    fontweight="bold",
    color="white",
    pad=20
)

x = np.arange(len(monthly_revenue))

y = monthly_revenue.values

monthly_chart.plot(
    x,
    y,
    color="#3B82F6",
    linewidth=3,
    marker="o",
    markersize=8
)

monthly_chart.fill_between(
    x,
    y,
    color="#3B82F6",
    alpha=0.18
)

monthly_chart.set_xticks(x)

monthly_chart.set_xticklabels(
    monthly_revenue.index,
    color="white",
    fontsize=10
)

monthly_chart.tick_params(axis="y", colors="white")

monthly_chart.grid(
    linestyle="--",
    alpha=0.25
)

monthly_chart.yaxis.set_major_formatter(
    FuncFormatter(lambda x, pos: f"₹{x/1_000_000:.0f}M")
)

# ==============================
# REVENUE BY CATEGORY
# ==============================

category_chart = fig.add_subplot(gs[6:14, 14:24])

category_chart.set_facecolor("#162033")

colors = [
    "#3B82F6",
    "#8B5CF6",
    "#06B6D4",
    "#22C55E",
    "#F59E0B",
    "#EC4899"
]

wedges, labels, percentages = category_chart.pie(
    category_revenue.values,

    # Category names OUTSIDE
    labels=category_revenue.index,

    # Percentage INSIDE each slice
    autopct="%1.1f%%",

    # This controls the percentage position
    pctdistance=0.80,

    # This controls category-name position
    labeldistance=1.18,

    startangle=90,

    colors=colors,

    # Donut thickness
    wedgeprops=dict(
        width=0.42,
        edgecolor="#162033",
        linewidth=1
    ),

    textprops=dict(
        color="white"
    )
)

# ==============================
# CATEGORY NAMES
# ==============================

for label in labels:
    label.set_color("white")
    label.set_fontsize(9)

# ==============================
# PERCENTAGE VALUES
# ==============================

for percentage in percentages:
    percentage.set_color("white")
    percentage.set_fontsize(8)
    percentage.set_fontweight("bold")
    percentage.set_horizontalalignment("center")
    percentage.set_verticalalignment("center")

# ==============================
# TITLE
# ==============================

category_chart.set_title(
    "Revenue by Category",
    fontsize=15,
    color="white",
    fontweight="bold",
    pad=18
)

# Keep donut perfectly circular
category_chart.set_aspect("equal")

# ==========================================================
# Top Stores by Revenue
# ==========================================================

store_chart = fig.add_subplot(gs[14:20, 0:12])

store_chart.set_facecolor("#162033")

top_stores = (
    store_revenue
    .sort_values(ascending=True)
    .tail(8)
)

bars = store_chart.barh(
    top_stores.index,
    top_stores.values,
    color="#3B82F6"
)

# Title
store_chart.set_title(
    "Top Stores by Revenue",
    fontsize=15,
    color="white",
    fontweight="bold",
    pad=24
)

# Axis labels
store_chart.tick_params(
    axis="y",
    colors="white",
    labelsize=9,
    pad=5
)

store_chart.tick_params(
    axis="x",
    colors="white",
    labelsize=8
)

store_chart.set_xlabel(
    "Revenue (₹)",
    color="white",
    fontsize=9,
    labelpad=8
)

# Grid
store_chart.grid(
    axis="x",
    linestyle="--",
    alpha=0.25
)

store_chart.set_axisbelow(True)

# Border
for spine in store_chart.spines.values():
    spine.set_color("#334155")

# Add revenue values at end of bars
for bar in bars:
    value = bar.get_width()

    store_chart.text(
        value + top_stores.max() * 0.01,
        bar.get_y() + bar.get_height() / 2,
        f"₹{value / 1e6:.1f}M",
        va="center",
        ha="left",
        color="white",
        fontsize=8
    )

# Give extra room for value labels
store_chart.set_xlim(
    0,
    top_stores.max() * 1.12
)

# Revenue labels
for bar in bars:
    width = bar.get_width()

    store_chart.text(
        width + top_stores.max() * 0.01,
        bar.get_y() + bar.get_height() / 2,
        f"₹{width / 1e6:.1f}M",
        va="center",
        color="white",
        fontsize=8
    )
    
    # ==========================================================
# TOP 10 PRODUCTS BY REVENUE
# ==========================================================

product_chart = fig.add_subplot(gs[15:20, 14:24])

product_chart.set_facecolor("#162033")

# Sort ascending so highest revenue appears at the top
top_products_display = (
    top_products
    .sort_values(ascending=True)
)

bars = product_chart.barh(
    top_products_display.index,
    top_products_display.values,
    color="#22C55E"
)

# ----------------------------------------------------------
# Title
# ----------------------------------------------------------

product_chart.set_title(
    "Top 10 Products by Revenue",
    fontsize=15,
    color="white",
    fontweight="bold",
    pad=14
)

# ----------------------------------------------------------
# Y-axis
# ----------------------------------------------------------

product_chart.tick_params(
    axis="y",
    colors="white",
    labelsize=9,
    pad=5
)

# ----------------------------------------------------------
# X-axis
# ----------------------------------------------------------

product_chart.tick_params(
    axis="x",
    colors="white",
    labelsize=8
)

product_chart.set_xlabel(
    "Revenue (₹)",
    color="white",
    fontsize=9,
    labelpad=8
)

# ----------------------------------------------------------
# Grid
# ----------------------------------------------------------

product_chart.grid(
    axis="x",
    linestyle="--",
    alpha=0.25
)

product_chart.set_axisbelow(True)

# ----------------------------------------------------------
# Border
# ----------------------------------------------------------

for spine in product_chart.spines.values():
    spine.set_color("#334155")

# ----------------------------------------------------------
# Revenue values
# ----------------------------------------------------------

for bar in bars:

    value = bar.get_width()

    product_chart.text(
        value + top_products_display.max() * 0.01,
        bar.get_y() + bar.get_height() / 2,
        f"₹{value / 1e6:.1f}M",
        va="center",
        ha="left",
        color="white",
        fontsize=8
    )

# Give labels some space
product_chart.set_xlim(
    0,
    top_products_display.max() * 1.12
)

# ==========================================================
# PAYMENT METHODS
# ==========================================================

payment_chart = fig.add_subplot(
    gs[22:28, 0:6]
)

payment_chart.set_facecolor("#162033")

payment_colors = [
    "#3B82F6",
    "#8B5CF6",
    "#06B6D4",
    "#22C55E",
    "#F59E0B"
]

wedges, labels, percentages = payment_chart.pie(
    payment_methods.values,
    labels=payment_methods.index,
    autopct="%1.1f%%",
    pctdistance=0.85,
    labeldistance=1.12,
    startangle=90,
    radius=1.15,
    colors=payment_colors,
    wedgeprops=dict(
        width=0.38,
        edgecolor="#162033",
        linewidth=1
    ),
    textprops=dict(
        color="white",
        fontsize=6
    )
)

# Payment method names
for label in labels:
    label.set_color("white")
    label.set_fontsize(8)

# Percentages
for percentage in percentages:
    percentage.set_color("white")
    percentage.set_fontsize(6)
    percentage.set_fontweight("bold")
    percentage.set_horizontalalignment("center")
    percentage.set_verticalalignment("center")

payment_chart.set_title(
    "Payment Methods",
    fontsize=14,
    color="white",
    fontweight="bold",
    pad=14
)

payment_chart.set_aspect("equal")

# ==========================================================
# ORDER STATUS
# ==========================================================

status_chart = fig.add_subplot(
    gs[22:28, 6:12]
)

status_chart.set_facecolor("#162033")

status_colors = [
    "#22C55E",   # Delivered
    "#F59E0B",   # Processing
    "#3B82F6",   # Shipped
    "#EF4444",   # Returned
    "#8B5CF6"    # Cancelled
]

wedges, labels, percentages = status_chart.pie(
    order_status.values,
    labels=order_status.index,
    autopct="%1.1f%%",
    pctdistance=0.85,
    labeldistance=1.12,
    startangle=90,
    radius=1.15,
    colors=status_colors,
    wedgeprops=dict(
        width=0.38,
        edgecolor="#162033",
        linewidth=1
    ),
    textprops=dict(
        color="white",
        fontsize=6
    )
)

# Order status names
for label in labels:
    label.set_color("white")
    label.set_fontsize(8)

# Percentage values
for percentage in percentages:
    percentage.set_color("white")
    percentage.set_fontsize(6)
    percentage.set_fontweight("bold")
    percentage.set_horizontalalignment("center")
    percentage.set_verticalalignment("center")

status_chart.set_title(
    "Order Status",
    fontsize=14,
    color="white",
    fontweight="bold",
    pad=14
)

status_chart.set_aspect("equal")

# ==========================================================
# REVENUE BY STATE
# ==========================================================

state_chart = fig.add_subplot(
    gs[22:28, 12:18]
)

state_chart.set_facecolor("#162033")

# Sort for horizontal bar chart
state_data = state_revenue.sort_values(ascending=True)

bars = state_chart.barh(
    state_data.index,
    state_data.values,
    color="#06B6D4"
)

# ----------------------------------------------------------
# Title
# ----------------------------------------------------------

state_chart.set_title(
    "Revenue by State",
    fontsize=14,
    color="white",
    fontweight="bold",
    pad=16
)

# ----------------------------------------------------------
# Axis
# ----------------------------------------------------------

state_chart.tick_params(
    axis="y",
    colors="white",
    labelsize=8
)

state_chart.tick_params(
    axis="x",
    colors="white",
    labelsize=7
)

state_chart.set_xlabel(
    "Revenue (₹)",
    color="white",
    fontsize=8,
    labelpad=6
)

# ----------------------------------------------------------
# Grid
# ----------------------------------------------------------

state_chart.grid(
    axis="x",
    linestyle="--",
    alpha=0.25
)

state_chart.set_axisbelow(True)

# ----------------------------------------------------------
# Border
# ----------------------------------------------------------

for spine in state_chart.spines.values():
    spine.set_color("#334155")

# ----------------------------------------------------------
# Revenue Values
# ----------------------------------------------------------

for bar in bars:

    value = bar.get_width()

    state_chart.text(
        value + state_data.max() * 0.01,
        bar.get_y() + bar.get_height() / 2,
        f"₹{value / 1e6:.1f}M",
        va="center",
        ha="left",
        color="white",
        fontsize=7
    )

# Give space for value labels
state_chart.set_xlim(
    0,
    state_data.max() * 1.15
)

# ==========================================================
# EXECUTIVE INSIGHTS
# ==========================================================

insights_chart = fig.add_subplot(
    gs[22:28, 18:24]
)

insights_chart.set_facecolor("#162033")

insights_chart.set_xticks([])
insights_chart.set_yticks([])

for spine in insights_chart.spines.values():
    spine.set_visible(False)

# ----------------------------------------------------------
# Background Box
# ----------------------------------------------------------

insight_box = patches.Rectangle(
    (0, 0),
    1,
    1,
    linewidth=1.5,
    edgecolor="#334155",
    facecolor="#162033",
    transform=insights_chart.transAxes
)

insights_chart.add_patch(insight_box)

# ----------------------------------------------------------
# Title
# ----------------------------------------------------------

insights_chart.text(
    0.5,
    0.84,
    "Executive Insights",
    ha="center",
    va="center",
    fontsize=15,
    color="white",
    fontweight="bold",
    transform=insights_chart.transAxes
)

# ----------------------------------------------------------
# Insights Text
# ----------------------------------------------------------

# ----------------------------------------------------------
# Insight Content
# ----------------------------------------------------------

insight_lines = [
    f"Top Category: {best_category}",
    f"Top Store: {best_store}",
    f"Top Product: {best_product}",
    f"Preferred Payment: {best_payment}",
    f"Delivery Rate: {delivery_rate:.1f}%"
]

y_positions = [0.68, 0.55, 0.42, 0.29, 0.16]

for text, y in zip(insight_lines, y_positions):

    insights_chart.text(
        0.5,
        y,
        text,
        ha="center",
        va="center",
        fontsize=9.5,
        color="#CBD5E1",
        transform=insights_chart.transAxes
    )
 # ==========================================================
# FOOTER
# ==========================================================

fig.text(
    0.5,
    0.025,
    "Created by Shreya Kumbharkar  |  SQL • Python • Pandas • Matplotlib",
    ha="center",
    va="center",
    fontsize=15,
    color="#64748B"
) 
    
# ==========================================================
# TEMPORARY SAVE (PREVIEW)
# ==========================================================

plt.savefig(
    SCREENSHOT_DIR / "dashboard_v2_preview.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nDashboard Preview Saved Successfully!")