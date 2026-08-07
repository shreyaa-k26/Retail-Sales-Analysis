import pandas as pd
import matplotlib.pyplot as plt
import os

# ============================
# Load Dataset
# ============================

customers = pd.read_csv("Dataset/customers.csv")
products = pd.read_csv("Dataset/products.csv")
orders = pd.read_csv("Dataset/orders.csv")
order_details = pd.read_csv("Dataset/order_details.csv")

# ============================
# Create Screenshots Folder
# ============================

os.makedirs("Screenshots", exist_ok=True)

# ============================
# Revenue Calculation
# ============================

sales = order_details.merge(
    products[['product_id', 'product_name', 'category', 'price']],
    on='product_id'
)

sales['Revenue'] = (
    sales['price']
    * sales['quantity']
    * (1 - sales['discount'] / 100)
)

# ============================
# Top 10 Products by Revenue
# ============================

top_products = (
    sales.groupby('product_name')['Revenue']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))
top_products.plot(kind='bar')
plt.title("Top 10 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig("Screenshots/top_10_products.png")
plt.close()

print("✅ Chart saved: Screenshots/top_10_products.png")

# ============================
# Revenue by Category
# ============================

category_revenue = (
    sales.groupby('category')['Revenue']
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
category_revenue.plot(kind='bar')
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.tight_layout()

plt.savefig("Screenshots/revenue_by_category.png")
plt.close()


# ============================
# Payment Method Distribution
# ============================

payment_counts = orders['payment_method'].value_counts()

plt.figure(figsize=(7,7))
payment_counts.plot(kind='pie', autopct='%1.1f%%')
plt.ylabel("")
plt.title("Payment Method Distribution")
plt.tight_layout()

plt.savefig("Screenshots/payment_method_distribution.png")
plt.close()


# ============================
# Order Status Distribution
# ============================

status_counts = orders['order_status'].value_counts()

plt.figure(figsize=(8,5))
status_counts.plot(kind='bar')
plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")
plt.tight_layout()

plt.savefig("Screenshots/order_status_distribution.png")
plt.close()


print("✅ Revenue by Category chart saved")
print("✅ Payment Method Distribution chart saved")
print("✅ Order Status Distribution chart saved")

# ============================
# Monthly Orders Trend
# ============================

orders['order_date'] = pd.to_datetime(orders['order_date'])

monthly_orders = (
    orders.groupby(orders['order_date'].dt.month_name())['order_id']
    .count()
    .reindex([
        'January','February','March','April','May','June',
        'July','August','September','October','November','December'
    ])
)

plt.figure(figsize=(10,5))
monthly_orders.plot(kind='line', marker='o')
plt.title("Monthly Orders Trend")
plt.xlabel("Month")
plt.ylabel("Number of Orders")
plt.grid(True)
plt.tight_layout()

plt.savefig("Screenshots/monthly_orders_trend.png")
plt.close()


# ============================
# Revenue by Store
# ============================

store_sales = (
    order_details
    .merge(products[['product_id','price']], on='product_id')
    .merge(orders[['order_id','store_id']], on='order_id')
)

store_sales['Revenue'] = (
    store_sales['price']
    * store_sales['quantity']
    * (1 - store_sales['discount']/100)
)

store_revenue = (
    store_sales.groupby('store_id')['Revenue']
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10,5))
store_revenue.plot(kind='bar')
plt.title("Revenue by Store")
plt.xlabel("Store ID")
plt.ylabel("Revenue")
plt.tight_layout()

plt.savefig("Screenshots/revenue_by_store.png")
plt.close()


# ============================
# Customer Age Distribution
# ============================

plt.figure(figsize=(8,5))
customers['age'].plot(kind='hist', bins=10)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.tight_layout()

plt.savefig("Screenshots/customer_age_distribution.png")
plt.close()


print("✅ Monthly Orders Trend chart saved")
print("✅ Revenue by Store chart saved")
print("✅ Customer Age Distribution chart saved")

# ============================
# Top 10 Customers by Spending
# ============================

customer_sales = (
    order_details
    .merge(products[['product_id', 'price']], on='product_id')
    .merge(orders[['order_id', 'customer_id']], on='order_id')
    .merge(customers[['customer_id', 'customer_name']], on='customer_id')
)

customer_sales['Revenue'] = (
    customer_sales['price']
    * customer_sales['quantity']
    * (1 - customer_sales['discount'] / 100)
)

top_customers = (
    customer_sales.groupby('customer_name')['Revenue']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))
top_customers.plot(kind='bar')
plt.title("Top 10 Customers by Spending")
plt.xlabel("Customer")
plt.ylabel("Revenue")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.savefig("Screenshots/top_customers.png")
plt.close()


# ============================
# Discount Distribution
# ============================

plt.figure(figsize=(8,5))
order_details['discount'].plot(kind='hist', bins=10)
plt.title("Discount Distribution")
plt.xlabel("Discount (%)")
plt.ylabel("Frequency")
plt.tight_layout()

plt.savefig("Screenshots/discount_distribution.png")
plt.close()


# ============================
# Top Categories by Quantity Sold
# ============================

category_quantity = (
    order_details
    .merge(products[['product_id', 'category']], on='product_id')
    .groupby('category')['quantity']
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
category_quantity.plot(kind='bar')
plt.title("Top Categories by Quantity Sold")
plt.xlabel("Category")
plt.ylabel("Quantity Sold")
plt.tight_layout()

plt.savefig("Screenshots/top_categories_quantity.png")
plt.close()


print("✅ Top Customers chart saved")
print("✅ Discount Distribution chart saved")
print("✅ Top Categories by Quantity Sold chart saved")