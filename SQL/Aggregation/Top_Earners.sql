SELECT MAX(months * salary) ||' '|| COUNT(*) FROM employee GROUP BY salary HAVING MAX(months * salary) = (SELECT MAX(months * salary) from employee);
