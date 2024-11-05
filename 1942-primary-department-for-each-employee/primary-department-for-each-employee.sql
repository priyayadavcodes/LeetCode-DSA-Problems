SELECT 
    e1.employee_id,
    (
        CASE
            WHEN e2.primary_flag IS NULL THEN e1.department_id
            WHEN e2.primary_flag IS NOT NULL AND e2.primary_flag = 'Y' THEN e2.department_id
        END
    ) AS department_id
FROM employee e1
LEFT JOIN (
    SELECT 
        * 
    FROM employee
    WHERE primary_flag = 'Y'
) AS e2 
ON e1.employee_id = e2.employee_id
GROUP BY e1.employee_id;