SELECT emp_low.name AS lower_earner, emp_high.name AS higher_earner
FROM EMPLOYEE AS emp_low
JOIN EMPLOYEE AS emp_high
    ON emp_low.salary < emp_high.salary
ORDER BY emp_low.id, emp_high.salary;
