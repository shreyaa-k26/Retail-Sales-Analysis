-- ============================================================
-- Query 1: Total Revenue Generated
-- ============================================================

SELECT
ROUND(SUM(p.price * od.quantity * (1 - od.discount/100)),2) AS total_revenue
FROM order_details od
JOIN products p
ON od.product_id = p.product_id;


-- ============================================================
-- Query 2: Top 10 Revenue Generating Products
-- ============================================================

SELECT
p.product_id,
p.product_name,
ROUND(SUM(p.price * od.quantity * (1 - od.discount/100)),2) AS revenue
FROM products p
JOIN order_details od
ON p.product_id = od.product_id
GROUP BY p.product_id, p.product_name
ORDER BY revenue DESC
LIMIT 10;


-- ============================================================
-- Query 3: Revenue by Category
-- ============================================================

SELECT
p.category,
ROUND(SUM(p.price * od.quantity * (1 - od.discount/100)),2) AS revenue
FROM products p
JOIN order_details od
ON p.product_id = od.product_id
GROUP BY p.category
ORDER BY revenue DESC;


-- ============================================================
-- Query 4: Top 10 Customers by Spending
-- ============================================================

SELECT
c.customer_id,
c.customer_name,
ROUND(SUM(p.price * od.quantity * (1 - od.discount/100)),2) AS total_spent
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN order_details od
ON o.order_id = od.order_id
JOIN products p
ON od.product_id = p.product_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_spent DESC
LIMIT 10;


-- ============================================================
-- Query 5: Revenue by Payment Method
-- ============================================================

SELECT
o.payment_method,
ROUND(SUM(p.price * od.quantity * (1 - od.discount/100)),2) AS revenue
FROM orders o
JOIN order_details od
ON o.order_id = od.order_id
JOIN products p
ON od.product_id = p.product_id
GROUP BY o.payment_method
ORDER BY revenue DESC;

-- ============================================================
-- Query 6: Revenue by Store
-- ============================================================

SELECT
    o.store_id,
    ROUND(SUM(p.price * od.quantity * (1 - od.discount/100)),2) AS revenue
FROM orders o
JOIN order_details od
    ON o.order_id = od.order_id
JOIN products p
    ON od.product_id = p.product_id
GROUP BY o.store_id
ORDER BY revenue DESC;


-- ============================================================
-- Query 7: Top 10 Best Selling Products (By Quantity)
-- ============================================================

SELECT
    p.product_id,
    p.product_name,
    SUM(od.quantity) AS total_quantity_sold
FROM products p
JOIN order_details od
    ON p.product_id = od.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_quantity_sold DESC
LIMIT 10;


-- ============================================================
-- Query 8: Average Discount by Category
-- ============================================================

SELECT
    p.category,
    ROUND(AVG(od.discount),2) AS average_discount
FROM products p
JOIN order_details od
    ON p.product_id = od.product_id
GROUP BY p.category
ORDER BY average_discount DESC;


-- ============================================================
-- Query 9: Revenue by Month
-- ============================================================

SELECT
    YEAR(o.order_date) AS order_year,
    MONTHNAME(o.order_date) AS month,
    ROUND(SUM(p.price * od.quantity * (1 - od.discount/100)),2) AS revenue
FROM orders o
JOIN order_details od
    ON o.order_id = od.order_id
JOIN products p
    ON od.product_id = p.product_id
GROUP BY YEAR(o.order_date), MONTH(o.order_date), MONTHNAME(o.order_date)
ORDER BY YEAR(o.order_date), MONTH(o.order_date);


-- ============================================================
-- Query 10: Top 10 Most Ordered Customers
-- ============================================================

SELECT
    c.customer_id,
    c.customer_name,
    COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_orders DESC
LIMIT 10;

-- ============================================================
-- Query 11: Top 10 Products with Highest Average Discount
-- ============================================================

SELECT
    p.product_name,
    ROUND(AVG(od.discount),2) AS average_discount
FROM products p
JOIN order_details od
    ON p.product_id = od.product_id
GROUP BY p.product_name
ORDER BY average_discount DESC
LIMIT 10;


-- ============================================================
-- Query 12: Number of Orders by Payment Method
-- ============================================================

SELECT
    payment_method,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY payment_method
ORDER BY total_orders DESC;


-- ============================================================
-- Query 13: Average Order Quantity by Product
-- ============================================================

SELECT
    p.product_name,
    ROUND(AVG(od.quantity),2) AS average_quantity
FROM products p
JOIN order_details od
    ON p.product_id = od.product_id
GROUP BY p.product_name
ORDER BY average_quantity DESC
LIMIT 10;


-- ============================================================
-- Query 14: Revenue by Supplier
-- ============================================================

SELECT
    p.supplier,
    ROUND(SUM(p.price * od.quantity * (1 - od.discount/100)),2) AS revenue
FROM products p
JOIN order_details od
    ON p.product_id = od.product_id
GROUP BY p.supplier
ORDER BY revenue DESC;


-- ============================================================
-- Query 15: Top 10 Most Expensive Products Sold
-- ============================================================

SELECT DISTINCT
    p.product_name,
    p.category,
    p.price
FROM products p
JOIN order_details od
    ON p.product_id = od.product_id
ORDER BY p.price DESC
LIMIT 10;

-- ============================================================
-- Query 16: Store-wise Total Quantity Sold
-- ============================================================

SELECT
    o.store_id,
    SUM(od.quantity) AS total_quantity_sold
FROM orders o
JOIN order_details od
    ON o.order_id = od.order_id
GROUP BY o.store_id
ORDER BY total_quantity_sold DESC;


-- ============================================================
-- Query 17: Category-wise Average Product Price
-- ============================================================

SELECT
    category,
    ROUND(AVG(price),2) AS average_price
FROM products
GROUP BY category
ORDER BY average_price DESC;


-- ============================================================
-- Query 18: Top 10 Customers by Quantity Purchased
-- ============================================================

SELECT
    c.customer_id,
    c.customer_name,
    SUM(od.quantity) AS total_quantity
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_details od
    ON o.order_id = od.order_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_quantity DESC
LIMIT 10;


-- ============================================================
-- Query 19: Product Sales Count
-- ============================================================

SELECT
    p.product_name,
    COUNT(od.order_id) AS number_of_sales
FROM products p
JOIN order_details od
    ON p.product_id = od.product_id
GROUP BY p.product_name
ORDER BY number_of_sales DESC
LIMIT 10;


-- ============================================================
-- Query 20: Average Revenue Per Order
-- ============================================================

SELECT
    ROUND(
        AVG(order_revenue), 2
    ) AS average_order_revenue
FROM
(
    SELECT
        od.order_id,
        SUM(p.price * od.quantity * (1 - od.discount/100)) AS order_revenue
    FROM order_details od
    JOIN products p
        ON od.product_id = p.product_id
    GROUP BY od.order_id
) AS revenue_per_order;

-- ============================================================
-- Query 21: Top 5 Stores by Revenue
-- ============================================================

SELECT
    o.store_id,
    ROUND(SUM(p.price * od.quantity * (1 - od.discount/100)),2) AS total_revenue
FROM orders o
JOIN order_details od
    ON o.order_id = od.order_id
JOIN products p
    ON od.product_id = p.product_id
GROUP BY o.store_id
ORDER BY total_revenue DESC
LIMIT 5;


-- ============================================================
-- Query 22: Revenue by Order Status
-- ============================================================

SELECT
    o.order_status,
    ROUND(SUM(p.price * od.quantity * (1 - od.discount/100)),2) AS total_revenue
FROM orders o
JOIN order_details od
    ON o.order_id = od.order_id
JOIN products p
    ON od.product_id = p.product_id
GROUP BY o.order_status
ORDER BY total_revenue DESC;


-- ============================================================
-- Query 23: Top 10 Highest Discounted Products
-- ============================================================

SELECT
    p.product_name,
    MAX(od.discount) AS highest_discount
FROM products p
JOIN order_details od
    ON p.product_id = od.product_id
GROUP BY p.product_name
ORDER BY highest_discount DESC
LIMIT 10;


-- ============================================================
-- Query 24: Monthly Order Count
-- ============================================================

SELECT
    YEAR(order_date) AS order_year,
    MONTHNAME(order_date) AS month,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY YEAR(order_date), MONTH(order_date), MONTHNAME(order_date)
ORDER BY YEAR(order_date), MONTH(order_date);


-- ============================================================
-- Query 25: Customer Lifetime Revenue
-- ============================================================

SELECT
    c.customer_id,
    c.customer_name,
    ROUND(SUM(p.price * od.quantity * (1 - od.discount/100)),2) AS lifetime_revenue
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_details od
    ON o.order_id = od.order_id
JOIN products p
    ON od.product_id = p.product_id
GROUP BY c.customer_id, c.customer_name
ORDER BY lifetime_revenue DESC;