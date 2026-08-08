# 🛍️ Retail Sales Analysis using SQL & Python

A complete **Retail Sales Analysis** project developed using **MySQL, SQL, Python, Pandas, and Matplotlib**.

This project simulates a real-world retail business environment by generating synthetic retail datasets, storing them in a relational MySQL database, performing SQL-based analysis, and creating professional business visualizations and an executive sales dashboard.

---

## 📌 Project Objectives

- Design a relational retail database using MySQL.
- Generate and manage retail sales data.
- Perform SQL-based business analysis.
- Analyze customer, product, store, and order performance.
- Calculate important business KPIs.
- Create data visualizations using Python.
- Build an Executive Sales Performance Dashboard.

---

## 🚀 Features

- ✅ Relational MySQL Database
- ✅ Synthetic Retail Dataset
- ✅ 75 SQL Queries
- ✅ Business KPI Analysis
- ✅ Revenue Analysis
- ✅ Customer Analysis
- ✅ Product Performance Analysis
- ✅ Store Performance Analysis
- ✅ Python Data Analysis using Pandas
- ✅ 10+ Business Visualizations
- ✅ Executive Sales Performance Dashboard

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| MySQL | Database Management |
| SQL | Data Analysis |
| Python | Data Processing |
| Pandas | Data Analysis |
| Matplotlib | Data Visualization |
| VS Code | Development Environment |

---

## 📂 Project Structure

```text
Retail-Sales-Analysis/
│
├── Dataset/
│   ├── customers.csv
│   ├── products.csv
│   ├── stores.csv
│   ├── orders.csv
│   └── order_details.csv
│
├── Python/
│   ├── data_analysis.py
│   ├── executive_dashboard.py
│   ├── executive_dashboard_v2.py
│   ├── generate_dataset.py
│   ├── visualization.py
│   └── requirements.txt
│
├── SQL/
│   ├── 01_create_database.sql
│   ├── 02_create_tables.sql
│   ├── 03_import_data.sql
│   ├── 04_basic_queries.sql
│   ├── 05_intermediate_queries.sql
│   └── 06_advanced_queries.sql
│
├── Screenshots/
│
└── README.md
🗄️ Database Tables

The project uses five relational tables:

Table	Description
customers	Stores customer information
products	Stores product details
stores	Stores store information
orders	Stores order information
order_details	Stores purchased products, quantity, and discount
📊 SQL Analysis

The project contains 75 SQL queries divided into three levels.

🔹 Basic Queries — 25
SELECT statements
WHERE clause
ORDER BY
LIMIT
DISTINCT
Aggregate functions
Filtering records
🔹 Intermediate Queries — 25
INNER JOIN
LEFT JOIN
GROUP BY
HAVING
Subqueries
Date functions
String functions
🔹 Advanced Queries — 25
Multi-table joins
Revenue analysis
Customer analysis
Product performance
Store performance
Sales trends
Business KPI analysis
🐍 Python Analysis

Python and Pandas are used for:

Dataset loading
Dataset exploration
Missing value detection
Revenue calculation
Business KPI analysis
Customer analysis
Product analysis
Store analysis
📈 Data Visualizations

The project generates multiple business visualizations using Matplotlib:

📊 Top 10 Products by Revenue
📊 Revenue by Category
🥧 Payment Method Distribution
📊 Order Status Distribution
📈 Monthly Orders Trend
📊 Revenue by Store
📊 Customer Age Distribution
📊 Top Customers by Spending
📊 Discount Distribution
📊 Top Categories by Quantity Sold
📊 Executive Sales Performance Dashboard

The project includes a professional Executive Sales Performance Dashboard created using Python, Pandas, NumPy, and Matplotlib.

The dashboard provides a consolidated view of retail business performance.

Dashboard KPIs
💰 Total Revenue
🛒 Total Orders
👥 Total Customers
📦 Total Products
🏪 Total Stores
💵 Average Order Value
Dashboard Analysis
📈 Monthly Revenue Trend
🥧 Revenue by Category
📊 Top Stores by Revenue
📊 Top 10 Products by Revenue
🥧 Payment Methods
🥧 Order Status
📊 Revenue by State
💡 Executive Business Insights
Dashboard Preview

📊 Business Insights

The analysis is based on:

Metric	Count
Customers	1,000
Products	100
Stores	20
Orders	10,000
Order Details	15,000

The project helps identify:

Top-performing products
Top-performing stores
Best-performing categories
Revenue distribution across states
Customer spending patterns
Payment method preferences
Order status distribution
Monthly revenue trends
Overall business performance
▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/shreyaa-k26/Retail-Sales-Analysis.git
cd Retail-Sales-Analysis

2️⃣ Install Python Dependencies
pip install -r Python/requirements.txt

3️⃣ Set Up MySQL Database

Open MySQL Workbench and execute the SQL files in the following order:

01_create_database.sql
02_create_tables.sql
03_import_data.sql

Import the CSV files into their respective tables when required.

4️⃣ Run SQL Analysis

Execute the following scripts:

04_basic_queries.sql
05_intermediate_queries.sql
06_advanced_queries.sql

5️⃣ Run Python Data Analysis
python Python/data_analysis.py

6️⃣ Generate Visualizations
python Python/visualization.py

7️⃣ Generate Executive Dashboard
python Python/executive_dashboard_v2.py

Generated charts and dashboard images are saved in the Screenshots/ folder.

📁 Dataset

The project contains synthetic retail data generated using Python.

Dataset Includes
1,000 Customers
100 Products
20 Stores
10,000 Orders
15,000 Order Details

The dataset contains information related to customers, products, stores, orders, payment methods, order status, prices, quantities, and discounts.

🔮 Future Enhancements
📊 Interactive Power BI dashboard
📈 Tableau business dashboard
🌐 Interactive Streamlit dashboard
🤖 Sales forecasting using machine learning
👥 Customer segmentation using clustering
🗄️ Live MySQL database integration
📱 Real-time business reporting
👩‍💻 Author
Shreya Sanjay Kumbharkar

Final Year B.E. Information Technology Student

Skills:

SQL
MySQL
Python
Pandas
Matplotlib
Data Analysis
Data Visualization
⭐ Project

If you found this project useful, consider giving the repository a ⭐ on GitHub.
