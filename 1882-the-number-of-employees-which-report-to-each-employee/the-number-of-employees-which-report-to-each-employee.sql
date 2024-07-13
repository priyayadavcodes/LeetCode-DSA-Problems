SELECT 
    employee_id, 
    name, 
    (SELECT COUNT(*) FROM Employees WHERE reports_to = e.employee_id) AS reports_count, 
    (SELECT ROUND(AVG(age)) FROM Employees WHERE reports_to = e.employee_id) AS average_age 
FROM 
    Employees e
WHERE 
    employee_id IN (SELECT DISTINCT reports_to FROM Employees)
ORDER BY 
    employee_id;
