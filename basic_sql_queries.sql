-- Basic SELECT
SELECT * FROM employees;

-- WHERE clause
SELECT name, salary 
FROM employees 
WHERE salary > 50000;

-- ORDER BY
SELECT name, salary 
FROM employees 
ORDER BY salary DESC;

-- GROUP BY
SELECT department, COUNT(*) 
FROM employees 
GROUP BY department;
