import pandas as pd

# ============================
# Load CSV Files
# ============================

customers = pd.read_csv("Dataset/customers.csv")
products = pd.read_csv("Dataset/products.csv")
stores = pd.read_csv("Dataset/stores.csv")
orders = pd.read_csv("Dataset/orders.csv")
order_details = pd.read_csv("Dataset/order_details.csv")

print("=" * 50)
print("Retail Sales Analysis")
print("=" * 50)

print("\nDatasets Loaded Successfully!\n")

# ============================
# Display Dataset Shapes
# ============================

print("Customers :", customers.shape)
print("Products  :", products.shape)
print("Stores    :", stores.shape)
print("Orders    :", orders.shape)
print("Order Details :", order_details.shape)

# ============================
# Dataset Information
# ============================

print("\n" + "=" * 50)
print("DATASET INFORMATION")
print("=" * 50)

print("\nCustomers")
print(customers.info())

print("\nProducts")
print(products.info())

print("\nStores")
print(stores.info())

print("\nOrders")
print(orders.info())

print("\nOrder Details")
print(order_details.info())


# ============================
# Missing Values
# ============================

print("\n" + "=" * 50)
print("MISSING VALUES")
print("=" * 50)

print("\nCustomers")
print(customers.isnull().sum())

print("\nProducts")
print(products.isnull().sum())

print("\nStores")
print(stores.isnull().sum())

print("\nOrders")
print(orders.isnull().sum())

print("\nOrder Details")
print(order_details.isnull().sum())

# ============================
# Business Analysis
# ============================

print("\n" + "=" * 50)
print("BUSINESS ANALYSIS")
print("=" * 50)

# Total Customers
print(f"\nTotal Customers : {customers['customer_id'].nunique()}")

# Total Products
print(f"Total Products  : {products['product_id'].nunique()}")

# Total Stores
print(f"Total Stores    : {stores['store_id'].nunique()}")

# Total Orders
print(f"Total Orders    : {orders['order_id'].nunique()}")

# Total Order Details
print(f"Total Order Details : {order_details.shape[0]}")

# Calculate Revenue
sales = order_details.merge(products[['product_id', 'price']], on='product_id')

sales['Revenue'] = (
    sales['price']
    * sales['quantity']
    * (1 - sales['discount'] / 100)
)

print(f"\nTotal Revenue : ₹{sales['Revenue'].sum():,.2f}")

print(f"Average Revenue Per Order : ₹{sales['Revenue'].mean():,.2f}")

print(f"Highest Revenue Generated : ₹{sales['Revenue'].max():,.2f}")

print(f"Lowest Revenue Generated  : ₹{sales['Revenue'].min():,.2f}")