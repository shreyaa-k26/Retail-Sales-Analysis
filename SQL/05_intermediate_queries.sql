-- ============================================
-- INTERMEDIATE SQL QUERIES
-- Retail Sales Analysis Project
-- ============================================

USE sales_analysis;

-- ============================================
-- Query 1: Customer Name with Order Details
-- ============================================

SELECT
    c.customer_name,
    o.order_id,
    o.order_date,
    o.payment_method,
    o.order_status,
    o.shipping_cost
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;

-- ============================================
-- Query 2: Product Name with Quantity Sold
-- ============================================

SELECT
    p.product_name,
    od.quantity
FROM products p
INNER JOIN order_details od
ON p.product_id = od.product_id;

-- ============================================
-- Query 3: Customer Name, Product Name and Quantity Purchased
-- ============================================

SELECT
    c.customer_name,
    p.product_name,
    od.quantity
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
INNER JOIN order_details od
ON o.order_id = od.order_id
INNER JOIN products p
ON od.product_id = p.product_id;

-- ============================================
-- Query 4: Total Quantity Sold Per Product
-- ============================================

SELECT
    p.product_id,
    p.product_name,
    SUM(od.quantity) AS total_quantity_sold
FROM products p
INNER JOIN order_details od
ON p.product_id = od.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_quantity_sold DESC;

-- ============================================
-- Query 5: Total Orders by Payment Method
-- ============================================

SELECT
    payment_method,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY payment_method
ORDER BY total_orders DESC;

-- ============================================
-- Query 6: Total Orders by Store
-- ============================================

SELECT
    store_id,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY store_id
ORDER BY total_orders DESC;

-- ============================================
-- Query 7: Average Shipping Cost by Payment Method
-- ============================================

SELECT
    payment_method,
    ROUND(AVG(shipping_cost), 2) AS average_shipping_cost
FROM orders
GROUP BY payment_method;

-- ============================================
-- Query 8: Total Customers in Each City
-- ============================================

SELECT
    city,
    COUNT(customer_id) AS total_customers
FROM customers
GROUP BY city
ORDER BY total_customers DESC;

-- ============================================
-- Query 9: Total Customers in Each State
-- ============================================

SELECT
    state,
    COUNT(customer_id) AS total_customers
FROM customers
GROUP BY state
ORDER BY total_customers DESC;

-- ============================================
-- Query 10: Total Orders by Order Status
-- ============================================

SELECT
    order_status,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY order_status
ORDER BY total_orders DESC;

-- ============================================
-- Query 11: Average Product Price by Category
-- ============================================

SELECT
    category,
    ROUND(AVG(price),2) AS average_price
FROM products
GROUP BY category
ORDER BY average_price DESC;

-- ============================================
-- Query 12: Top 10 Most Expensive Products
-- ============================================

SELECT
    product_name,
    category,
    price
FROM products
ORDER BY price DESC
LIMIT 10;

-- ============================================
-- Query 13: Customers by Gender
-- ============================================

SELECT
    gender,
    COUNT(customer_id) AS total_customers
FROM customers
GROUP BY gender;

-- ============================================
-- Query 14: Average Age by State
-- ============================================

SELECT
    state,
    ROUND(AVG(age),1) AS average_age
FROM customers
GROUP BY state
ORDER BY average_age DESC;

-- ============================================
-- Query 15: Top 10 Highest Shipping Cost Orders
-- ============================================

SELECT
    order_id,
    shipping_cost,
    order_status
FROM orders
ORDER BY shipping_cost DESC
LIMIT 10;


-- ============================================
-- Query 16: Number of Products in Each Category
-- ============================================

SELECT
    category,
    COUNT(product_id) AS total_products
FROM products
GROUP BY category
ORDER BY total_products DESC;


-- ============================================
-- Query 17: Total Orders by Year
-- ============================================

SELECT
    YEAR(order_date) AS order_year,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY YEAR(order_date)
ORDER BY order_year;


-- ============================================
-- Query 18: Total Orders by Month
-- ============================================

SELECT
    MONTHNAME(order_date) AS month,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY MONTH(order_date), MONTHNAME(order_date)
ORDER BY MONTH(order_date);


-- ============================================
-- Query 19: Average Shipping Cost by Order Status
-- ============================================

SELECT
    order_status,
    ROUND(AVG(shipping_cost),2) AS average_shipping_cost
FROM orders
GROUP BY order_status
ORDER BY average_shipping_cost DESC;

-- ============================================
-- Query 20: Total Orders by Customer
-- ============================================

SELECT
    customer_id,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY customer_id
ORDER BY total_orders DESC;


-- ============================================
-- Query 21: Customers with More Than 10 Orders
-- ============================================

SELECT
    customer_id,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY customer_id
HAVING COUNT(order_id) > 10
ORDER BY total_orders DESC;


-- ============================================
-- Query 22: Average Product Price by Supplier
-- ============================================

SELECT
    supplier,
    ROUND(AVG(price),2) AS average_price
FROM products
GROUP BY supplier
ORDER BY average_price DESC;


-- ============================================
-- Query 23: Store-wise Average Shipping Cost
-- ============================================

SELECT
    store_id,
    ROUND(AVG(shipping_cost),2) AS average_shipping_cost
FROM orders
GROUP BY store_id
ORDER BY average_shipping_cost DESC;


-- ============================================
-- Query 24: Total Customers by Age Group
-- ============================================

SELECT
CASE
    WHEN age < 20 THEN 'Below 20'
    WHEN age BETWEEN 20 AND 29 THEN '20-29'
    WHEN age BETWEEN 30 AND 39 THEN '30-39'
    WHEN age BETWEEN 40 AND 49 THEN '40-49'
    ELSE '50+'
END AS age_group,
COUNT(*) AS total_customers
FROM customers
GROUP BY age_group
ORDER BY age_group;


-- ============================================
-- Query 25: Top 10 Customers by Number of Orders
-- ============================================

SELECT
    customer_id,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY customer_id
ORDER BY total_orders DESC
LIMIT 10;