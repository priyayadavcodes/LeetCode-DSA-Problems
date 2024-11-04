select 
e2.employee_id,
e2.name,
count(e1.age) as reports_count,
Round(avg(e1.age)) as average_age
from 
employees e1
left join employees e2
on e1.reports_to = e2.employee_id
where e2.employee_id is not null 
group by e2.employee_id 
order by e2.employee_id