import pandas as pd
import random
import os
from faker import Faker
from datetime import datetime, timedelta

fake = Faker("en_IN")
random.seed(42)

# -----------------------------
# Create Dataset Folder
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(BASE_DIR, "..", "Dataset")
os.makedirs(DATASET_DIR, exist_ok=True)

# -----------------------------
# Configuration
# -----------------------------
NUM_CUSTOMERS = 1000
NUM_PRODUCTS = 100
NUM_STORES = 20
NUM_ORDERS = 10000
NUM_ORDER_DETAILS = 15000

# -----------------------------
# Product Categories
# -----------------------------
categories = {
    "Electronics": ["Laptop", "Smartphone", "Tablet", "Headphones", "Smartwatch"],
    "Fashion": ["T-Shirt", "Jeans", "Shoes", "Jacket", "Watch"],
    "Grocery": ["Rice", "Sugar", "Oil", "Tea", "Coffee"],
    "Home Appliances": ["Mixer", "Iron", "Fan", "Microwave", "Vacuum Cleaner"],
    "Books": ["Novel", "Dictionary", "Notebook", "Story Book", "Magazine"],
    "Sports": ["Football", "Cricket Bat", "Tennis Racket", "Yoga Mat", "Dumbbell"]
}

brands = [
    "Samsung", "Apple", "Dell", "HP", "Nike", "Adidas",
    "Prestige", "LG", "Sony", "Puma", "Lenovo", "Boat"
]

suppliers = [
    "ABC Traders", "Global Distributors", "Retail Hub",
    "Prime Suppliers", "Metro Wholesale"
]

# -----------------------------
# Generate Products
# -----------------------------
products = []

for pid in range(1, NUM_PRODUCTS + 1):
    category = random.choice(list(categories.keys()))
    product = random.choice(categories[category])

    products.append({
        "product_id": pid,
        "product_name": product,
        "category": category,
        "brand": random.choice(brands),
        "price": random.randint(200, 80000),
        "stock_quantity": random.randint(20, 500),
        "supplier": random.choice(suppliers)
    })

products_df = pd.DataFrame(products)

# -----------------------------
# Generate Stores
# -----------------------------
cities = [
    ("Pune", "Maharashtra"),
    ("Mumbai", "Maharashtra"),
    ("Nagpur", "Maharashtra"),
    ("Delhi", "Delhi"),
    ("Bengaluru", "Karnataka"),
    ("Hyderabad", "Telangana"),
    ("Chennai", "Tamil Nadu"),
    ("Ahmedabad", "Gujarat"),
    ("Jaipur", "Rajasthan"),
    ("Lucknow", "Uttar Pradesh"),
    ("Indore", "Madhya Pradesh"),
    ("Kolkata", "West Bengal"),
    ("Surat", "Gujarat"),
    ("Bhopal", "Madhya Pradesh"),
    ("Patna", "Bihar"),
    ("Goa", "Goa"),
    ("Kochi", "Kerala"),
    ("Chandigarh", "Punjab"),
    ("Visakhapatnam", "Andhra Pradesh"),
    ("Mysuru", "Karnataka")
]

stores = []

for sid, (city, state) in enumerate(cities, start=1):
    stores.append({
        "store_id": sid,
        "store_name": f"Retail Store {sid}",
        "city": city,
        "state": state
    })

stores_df = pd.DataFrame(stores)

print("✅ Products Generated:", len(products_df))
print("✅ Stores Generated:", len(stores_df))
# -----------------------------
# Generate Customers
# -----------------------------
customers = []

customer_cities = [
    ("Pune", "Maharashtra"),
    ("Mumbai", "Maharashtra"),
    ("Nagpur", "Maharashtra"),
    ("Delhi", "Delhi"),
    ("Bengaluru", "Karnataka"),
    ("Hyderabad", "Telangana"),
    ("Chennai", "Tamil Nadu"),
    ("Ahmedabad", "Gujarat"),
    ("Jaipur", "Rajasthan"),
    ("Lucknow", "Uttar Pradesh"),
    ("Indore", "Madhya Pradesh"),
    ("Kolkata", "West Bengal"),
    ("Surat", "Gujarat"),
    ("Patna", "Bihar"),
    ("Goa", "Goa")
]

for cid in range(1, NUM_CUSTOMERS + 1):

    gender = random.choice(["Male", "Female"])

    if gender == "Male":
        name = fake.name_male()
    else:
        name = fake.name_female()

    city, state = random.choice(customer_cities)

    customers.append({
        "customer_id": cid,
        "customer_name": name,
        "gender": gender,
        "age": random.randint(18, 65),
        "city": city,
        "state": state
    })

customers_df = pd.DataFrame(customers)

print("✅ Customers Generated:", len(customers_df))
# -----------------------------
# Generate Orders
# -----------------------------
payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Cash",
    "Net Banking"
]

order_statuses = [
    "Delivered",
    "Shipped",
    "Processing",
    "Cancelled",
    "Returned"
]

orders = []

start_date = datetime(2024, 1, 1)

for oid in range(1, NUM_ORDERS + 1):

    order_date = start_date + timedelta(days=random.randint(0, 730))

    orders.append({
        "order_id": oid,
        "customer_id": random.randint(1, NUM_CUSTOMERS),
        "store_id": random.randint(1, NUM_STORES),
        "order_date": order_date.strftime("%Y-%m-%d"),
        "payment_method": random.choice(payment_methods),
        "order_status": random.choices(
            order_statuses,
            weights=[70, 10, 10, 5, 5],
            k=1
        )[0],
        "shipping_cost": round(random.uniform(40, 250), 2)
    })

orders_df = pd.DataFrame(orders)

print("✅ Orders Generated:", len(orders_df))
# -----------------------------
# Generate Order Details
# -----------------------------
order_details = []

for did in range(1, NUM_ORDER_DETAILS + 1):

    order_details.append({
        "detail_id": did,
        "order_id": random.randint(1, NUM_ORDERS),
        "product_id": random.randint(1, NUM_PRODUCTS),
        "quantity": random.randint(1, 5),
        "discount": random.choice([0, 5, 10, 15, 20])
    })

order_details_df = pd.DataFrame(order_details)

print("✅ Order Details Generated:", len(order_details_df))
# -----------------------------
# Export CSV Files
# -----------------------------
customers_df.to_csv(
    os.path.join(DATASET_DIR, "customers.csv"),
    index=False
)

products_df.to_csv(
    os.path.join(DATASET_DIR, "products.csv"),
    index=False
)

stores_df.to_csv(
    os.path.join(DATASET_DIR, "stores.csv"),
    index=False
)

orders_df.to_csv(
    os.path.join(DATASET_DIR, "orders.csv"),
    index=False
)

order_details_df.to_csv(
    os.path.join(DATASET_DIR, "order_details.csv"),
    index=False
)

print("\n All CSV files generated successfully!")
print(f" Location: {DATASET_DIR}")