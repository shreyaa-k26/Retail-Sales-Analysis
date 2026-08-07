# 🛍️ Retail Sales Analysis using SQL & Python

A complete **Retail Sales Analysis** project developed using **MySQL, Python (Pandas), and Matplotlib**. This project demonstrates database design, SQL querying, data analysis, and data visualization to extract meaningful business insights from retail sales data.

The project simulates a real-world retail business environment by generating synthetic datasets, storing them in a MySQL database, analyzing sales using SQL, and visualizing key business metrics using Python.

---

## 📌 Project Objectives

- Design a relational retail database in MySQL.
- Import and manage retail sales datasets.
- Perform SQL-based business analysis.
- Analyze customer, product, and sales performance.
- Generate business insights using Python.
- Create professional data visualizations.

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
- ✅ 10 Business Visualizations using Matplotlib

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
├── Python/
├── SQL/
├── Screenshots/
├── README.md
└── requirements.txt
```
---

# 🗄️ Database Tables

The project uses five relational tables:

| Table | Description |
|-------|-------------|
| customers | Stores customer information |
| products | Stores product details |
| stores | Stores store information |
| orders | Stores order details |
| order_details | Stores purchased products, quantity, and discount |

---

# 📊 SQL Analysis

The project contains **75 SQL queries** divided into three levels:

## Basic Queries (25)

- SELECT statements
- WHERE clause
- ORDER BY
- LIMIT
- DISTINCT
- Aggregate Functions
- Filtering Records

## Intermediate Queries (25)

- INNER JOIN
- LEFT JOIN
- GROUP BY
- HAVING
- Subqueries
- Date Functions
- String Functions

## Advanced Queries (25)

- Multi-table Joins
- Revenue Analysis
- Customer Analysis
- Product Performance
- Store Performance
- Sales Trends
- Business KPI Analysis

---

# 🐍 Python Analysis

The project performs the following analysis using **Pandas**:

- Dataset Loading
- Dataset Exploration
- Missing Value Detection
- Business KPI Analysis
- Revenue Calculation
- Customer Analysis
- Product Analysis
- Store Analysis

---

# 📈 Data Visualizations

The project generates the following charts:

- 📊 Top 10 Products by Revenue
- 📊 Revenue by Category
- 🥧 Payment Method Distribution
- 📊 Order Status Distribution
- 📈 Monthly Orders Trend
- 📊 Revenue by Store
- 📊 Customer Age Distribution
- 📊 Top Customers by Spending
- 📊 Discount Distribution
- 📊 Top Categories by Quantity Sold

---

# ▶️ How to Run the Project

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Retail-Sales-Analysis.git
cd Retail-Sales-Analysis
```

---

## 2️⃣ Install Python Dependencies

```bash
pip install -r Python/requirements.txt
```

---

## 3️⃣ Import the Dataset into MySQL

- Open MySQL Workbench.
- Create the `sales_analysis` database.
- Execute:
  - `01_create_database.sql`
  - `02_create_tables.sql`
- Import the CSV files into their respective tables.
- Execute:
  - `03_import_data.sql`

---

## 4️⃣ Run SQL Queries

Execute the SQL scripts in the following order:

- `04_basic_queries.sql`
- `05_intermediate_queries.sql`
- `06_advanced_queries.sql`

---

## 5️⃣ Run Python Analysis

```bash
python Python/data_analysis.py
```

---

## 6️⃣ Generate Visualizations

```bash
python Python/visualization.py
```

All generated charts will be saved in the **Screenshots** folder.

---

# 📸 Generated Visualizations

The project generates the following visualizations:

- Top 10 Products by Revenue
- Revenue by Category
- Payment Method Distribution
- Order Status Distribution
- Monthly Orders Trend
- Revenue by Store
- Customer Age Distribution
- Top Customers by Spending
- Discount Distribution
- Top Categories by Quantity Sold

---

# 📈 Key Business Insights

- Analyzed sales data of **1,000 customers**, **100 products**, **20 stores**, **10,000 orders**, and **15,000 order details**.
- Calculated total revenue and average revenue.
- Identified top-performing products and customers.
- Compared revenue across product categories and stores.
- Analyzed order status and payment method distribution.
- Visualized customer demographics and sales trends.

---

# 🔮 Future Enhancements

- Build an interactive Power BI dashboard.
- Develop a Tableau dashboard for business reporting.
- Integrate the project with a live MySQL database.
- Create an interactive web dashboard using Streamlit.
- Add machine learning models for sales forecasting.
- Perform customer segmentation using clustering algorithms.

---

# 👩‍💻 Author

**Shreya Sanjay Kumbharkar**

Final Year B.E. Information Technology Student

### Skills

- SQL
- MySQL
- Python
- Pandas
- Matplotlib
- Data Analysis
- Data Visualization

---

# ⭐ If you found this project helpful, consider giving it a star on GitHub!