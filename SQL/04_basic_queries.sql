-- ============================================
-- BASIC SQL QUERIES
-- Retail Sales Analysis Project
-- ============================================

USE sales_analysis;

-- ============================================
-- Query 1: Display first 10 customers
-- ============================================

SELECT *
FROM customers
LIMIT 10;

-- ============================================
-- Query 2: Display all products
-- ============================================

SELECT *
FROM products;

-- ============================================
-- Query 3: Display all stores
-- ============================================

SELECT *
FROM stores;

-- ============================================
-- Query 4: Display first 10 orders
-- ============================================

SELECT *
FROM orders
LIMIT 10;

-- ============================================
-- Query 5: Count total customers
-- ============================================

SELECT COUNT(*) AS Total_Customers
FROM customers;

-- ============================================
-- Query 6: Count total products
-- ============================================

SELECT COUNT(*) AS Total_Products
FROM products;

-- ============================================
-- Query 7: Count total stores
-- ============================================

SELECT COUNT(*) AS Total_Stores
FROM stores;

-- ============================================
-- Query 8: Count total orders
-- ============================================

SELECT COUNT(*) AS Total_Orders
FROM orders;

-- ============================================
-- Query 9: Count total order details
-- ============================================

SELECT COUNT(*) AS Total_Order_Details
FROM order_details;

-- ============================================
-- Query 10: Display unique product categories
-- ============================================

SELECT DISTINCT category
FROM products;

-- ============================================
-- Query 11: Display products sorted by price (Highest to Lowest)
-- ============================================

SELECT *
FROM products
ORDER BY price DESC;

-- ============================================
-- Query 12: Display products sorted by price (Lowest to Highest)
-- ============================================

SELECT *
FROM products
ORDER BY price ASC;

-- ============================================
-- Query 13: Display Male Customers
-- ============================================

SELECT *
FROM customers
WHERE gender = 'Male';

-- ============================================
-- Query 14: Display Female Customers
-- ============================================

SELECT *
FROM customers
WHERE gender = 'Female';

-- ============================================
-- Query 15: Display Customers Older Than 40
-- ============================================

SELECT *
FROM customers
WHERE age > 40;

-- ============================================
-- Query 16: Display Products Costing More Than 1000
-- ============================================

SELECT *
FROM products
WHERE price > 1000;

-- ============================================
-- Query 17: Display Products Between 500 and 1000
-- ============================================

SELECT *
FROM products
WHERE price BETWEEN 500 AND 1000;

-- ============================================
-- Query 18: Display Customers from Mumbai
-- ============================================

SELECT *
FROM customers
WHERE city = 'Mumbai';

-- ============================================
-- Query 19: Display Customers from Maharashtra
-- ============================================

SELECT *
FROM customers
WHERE state = 'Maharashtra';

-- ============================================
-- Query 20: Display Electronics Products
-- ============================================

SELECT *
FROM products
WHERE category = 'Electronics';

-- ============================================
-- Query 21: Display Customers Aged Between 25 and 35
-- ============================================

SELECT *
FROM customers
WHERE age BETWEEN 25 AND 35;

-- ============================================
-- Query 22: Display Products Starting with 'S'
-- ============================================

SELECT *
FROM products
WHERE product_name LIKE 'S%';

-- ============================================
-- Query 23: Display Customers Whose Name Ends with 'a'
-- ============================================

SELECT *
FROM customers
WHERE customer_name LIKE '%a';

-- ============================================
-- Query 24: Display Products with Price Less Than 500
-- ============================================

SELECT *
FROM products
WHERE price < 500;

-- ============================================
-- Query 25: Display Orders Placed After 2024-06-01
-- ============================================

SELECT *
FROM orders
WHERE order_date > '2024-06-01';