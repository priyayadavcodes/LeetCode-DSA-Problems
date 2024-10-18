# Write your MySQL query statement below
select 
v.customer_id,
COUNT(CASE 
    WHEN t.visit_id IS NULL THEN 1 
    END) AS count_no_trans
from visits v
left join transactions t
on v.visit_id = t.visit_id
where t.visit_id is null
group by customer_id 
