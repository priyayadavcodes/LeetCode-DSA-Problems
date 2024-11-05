SELECT e1.employee_id,
case
    when e2.department_id is null then e1.department_id
    else e2.department_id
end as department_id
FROM employee e1
LEFT JOIN (
    SELECT 
        * 
    FROM employee
    WHERE primary_flag = 'Y'
) AS e2 
ON e1.employee_id = e2.employee_id
group by e1.employee_id 
