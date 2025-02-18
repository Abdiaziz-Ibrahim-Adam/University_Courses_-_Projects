/*
    Fill in the queries between the "SELECT QUERY#" and "SELECT END",
    see 'Query 0' for a sample answer.
    If there are any uncertainties contact the TAs.
*/

SELECT 'Query 0'; -- Do not remove
-- Select the product names of all products (example)
SELECT product_name FROM products;

SELECT 'END'; -- Do not remove

/*
    Below, we will be looking at the formatting of answers. This will be
    of importance 
*/

SELECT 'Query 1'; -- Do not remove
/*
    Select the names and prices of all products, in two columns
    (i.e. the answer should be on the form |apple|50|)
*/
SELECT product_name, unit_price FROM products;
SELECT 'END'; -- Do not remove

SELECT 'Query 2'; -- Do not remove
/*
    Do the same again, but now flip the order of name and price
    (i.e. the answer should be on the form |50|apple|)
*/
SELECT unit_price, product_name FROM products;
SELECT 'END'; -- Do not remove

SELECT 'Query 3'; -- Do not remove
/*
    Do the same again, but now get the result in only one column,
    with the two values separated by a comma
    (i.e. the answer should be on the form (apple,50))
*/
SELECT product_name || ',' || unit_price AS single_column FROM products;
SELECT 'END'; -- Do not remove

SELECT 'Query 4'; -- Do not remove
/*
    Do the same as in Query 3, but rename the resulting column to "query_4_results"
    (i.e. the answer's header should say "query_4_results")
*/
SELECT product_name || ',' || unit_price AS query_4_results FROM products;
SELECT 'END'; -- Do not remove

/*
    Below, we will be introducing you to different SQL statements. 
*/

SELECT 'Query 5'; -- Do not remove
/*
    WHERE, AND, NOT
    What: Select the products from the category with ID 1 and where discontinued equals 1.
    Format: none (SELECT *)
*/
SELECT * FROM products WHERE category_id = 1 AND discontinued = 1;
SELECT 'END'; -- Do not remove

SELECT 'Query 6'; -- Do not remove
/*
    COUNT(attribute), GROUP BY(attribute)
    What: Select the number of products within each category.
    Format: category_id | * count * 
*/
SELECT category_id, COUNT(*) AS count FROM products GROUP BY category_id;
SELECT 'END'; -- Do not remove

SELECT 'Query 7'; -- Do not remove
/*
    HAVING
    What: Repeat 6, but only those categories with less than 10 products.
    Format: category_id | * count * 
*/
SELECT category_id, COUNT(*) AS count FROM products GROUP BY category_id HAVING COUNT(*) < 10;
SELECT 'END'; -- Do not remove

SELECT 'Query 8'; -- Do not remove
/*
    ORDER BY
    What: Repeat 7, order the by count ascending.
    Format: category_id | * count * 
*/
SELECT category_id, COUNT(*) AS count FROM products GROUP BY category_id HAVING COUNT(*) < 10 ORDER BY count ASC;
SELECT 'END'; -- Do not remove

SELECT 'Query 9'; -- Do not remove
/*
    FROM (multiple tables)
    What: Select the number of products within each category, using the category name.
    Format: category_name | * count * 
*/
SELECT categories.category_name, COUNT(products.product_id) AS count 
FROM products, categories 
WHERE products.category_id = categories.category_id 
GROUP BY categories.category_name;
SELECT 'END'; -- Do not remove

SELECT 'Query 10'; -- Do not remove
/*
    JOIN
    What: Repeat 9, without selecting from categories, use join instead.
    Format: category_name | * count * 
*/
SELECT categories.category_name, COUNT(products.product_id) AS count 
FROM products 
JOIN categories ON products.category_id = categories.category_id 
GROUP BY categories.category_name;
SELECT 'END'; -- Do not remove
