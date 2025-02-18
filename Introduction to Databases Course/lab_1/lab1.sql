/*
    Fill in the queries between the "SELECT QUERY#" and "SELECT END",
    see 'Query 0' for a sample answer.
    If there are any uncertainties contact the TAs.

    You must use joins when filtering, hard coded ids and similar are
    not acceptable. Avoid using natural joins for clarity.

    Structure your queries in a readable format, you do not have
    to use capitalized keywords - Just be consistent.
*/

SELECT 'Query 0'; -- Do not remove
-- Select the product names of all products
SELECT product_name FROM products;

SELECT 'END'; -- Do not remove

SELECT 'Query 1'; -- Do not remove
/*
    What:       Select the product names and their category for products with a supplier
                located in Sweden.
    Format:     | product_name | category_id | country |
*/
SELECT p.product_name, p.category_id, s.country
FROM products p
JOIN suppliers s ON p.supplier_id = s.supplier_id
WHERE s.country = 'Sweden';
SELECT 'END'; -- Do not remove


SELECT 'Query 2'; -- Do not remove
/*
    What:       Select the product name and the name of their supplier in the
                categories 'Meat/Poultry', 'Seafood' or 'Produce'.
    Format:     | product_name | company_name | category_name |
*/
SELECT p.product_name, s.company_name, c.category_name
FROM products p
JOIN suppliers s ON p.supplier_id = s.supplier_id
JOIN categories c ON p.category_id = c.category_id
WHERE c.category_name IN ('Meat/Poultry', 'Seafood', 'Produce');
SELECT 'END'; -- Do not remove

SELECT 'Query 3'; -- Do not remove
/*
    What:       Select the product names and unit prices of all products in the category
                'Seafood' excluding products supplied by the country of 'Japan'.
                Order by unit price descending.
    Format:     | product_name | unit_price | category_name | country |
*/
SELECT p.product_name, p.unit_price, c.category_name, s.country
FROM products p
JOIN suppliers s ON p.supplier_id = s.supplier_id
JOIN categories c ON p.category_id = c.category_id
WHERE category_name = 'Seafood' AND s.country <> 'Japan'
ORDER BY p.unit_price DESC;
SELECT 'END'; -- Do not remove

SELECT 'Query 4'; -- Do not remove
/*
    What:       Retrieve the names of employees who have the phrase "BA degree" or "BS degree" in their note.
    Format:     | first_name | last_name | notes |
*/
SELECT e.first_name, e.last_name, e.notes
FROM employees e 
WHERE e.notes LIKE '%BA degree%' OR e.notes LIKE '%BS degree%'; 
SELECT 'END'; -- Do not remove

SELECT 'Query 5'; -- Do not remove
/*
    What:       Retrieve the number of orders placed by each customer and ordered by the number of orders for
                each customer in descending order.
                OBS: There exists orders for which customer_id is NULL, include these and let customer_id be NULL.
    Format:     | customer_id | * order_count * |
*/
SELECT o.customer_id, COUNT(o.order_id) AS order_count
FROM orders o
GROUP BY o.customer_id 
ORDER BY order_count DESC;
SELECT 'END'; -- Do not remove

SELECT 'Query 6'; -- Do not remove
/*

    What:       Repeat query 5 but only report for customers with more than 5 orders who are not in Venezuela, 
                Brazil or Argentina.
    Format:     | customer_id | country | * order_count * |
*/
SELECT c.customer_id, c.country, COUNT(o.order_id) AS order_count
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE c.country NOT IN ('Venezuela', 'Brazil', 'Argentina')
GROUP BY c.customer_id, c.country
HAVING COUNT(o.order_id) > 5;
SELECT 'END'; -- Do not remove

SELECT 'Query 7'; -- Do not remove
/*
    What:       List the product name and category of the products which have no orders between 1996-07-10 and 1996-09-09.
                Exclude duplicates and order by product_name ascending.
    Format:     | product_name | category_name | 
*/
SELECT p.product_name, c.category_name
FROM products p
JOIN categories c ON p.category_id = c.category_id
WHERE p.product_id NOT IN (
    SELECT DISTINCT od.product_id 
    FROM order_details od
    JOIN orders o ON od.order_id = o.order_id
    WHERE o.order_date BETWEEN '1996-07-10' AND '1996-09-09'
);
SELECT 'END'; -- Do not remove

SELECT 'Query 8'; -- Do not remove
/*
    What:       Show the number of orders per employee for order dates between 1996-07-01 and 1996-07-15.
                If the answer is 0 for an employee, include that in the answer.
    Format:     | employee_id | * order_count * | 
*/
SELECT e.employee_id, COUNT(o.order_id) AS order_count
FROM employees e
LEFT JOIN orders o ON e.employee_id = o.employee_id 
AND o.order_date BETWEEN '1996-07-01' AND '1996-07-15'
GROUP BY e.employee_id;
SELECT 'END'; -- Do not remove

SELECT 'Query 9'; -- Do not remove
/*
    What:       For each product report their current unit price and the max, min, average, median and count of unit prices from actual orders.
                (Hint use PostgreSQL's PERCENTILE_CONT(0.5) to calculate median)
    Format:     | product_id | unit_price | * max_price * | * min_price * | * average * | * median * | * price_count * |
*/
SELECT p.product_id, p.unit_price, 
       MAX(od.unit_price) AS max_price, 
       MIN(od.unit_price) AS min_price, 
       AVG(od.unit_price) AS average, 
       PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY od.unit_price) AS median, 
       COUNT(od.unit_price) AS price_count
FROM products p
LEFT JOIN order_details od ON p.product_id = od.product_id
GROUP BY p.product_id, p.unit_price;
SELECT 'END'; -- Do not remove

SELECT 'Query 10'; -- Do not remove
/*
    What:       Give names and titles of all the employees under the authority of Andrew Fuller.
                Note that if we added additional employees that were any level below Andrew, they should be included in this result
    Format:     | first_name | last_name |        * reports_to *        |
 */
WITH RECURSIVE employee_hierarchy AS (
    SELECT employee_id, first_name, last_name, reports_to
    FROM employees
    WHERE reports_to = (SELECT employee_id FROM employees WHERE first_name = 'Andrew' AND last_name = 'Fuller')
    UNION ALL
    SELECT e.employee_id, e.first_name, e.last_name, e.reports_to
    FROM employees e
    JOIN employee_hierarchy eh ON e.reports_to = eh.employee_id
)
SELECT first_name, last_name, reports_to FROM employee_hierarchy;
SELECT 'END'; -- Do not remove