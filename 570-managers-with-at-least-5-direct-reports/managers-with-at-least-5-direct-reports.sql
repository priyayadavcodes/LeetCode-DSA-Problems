with tab as (select
e2.name,
count(e1.managerId) as num
from 
employee e1
join employee e2
on e1.managerId = e2.id
group by e1.managerId)

select name
from tab 
where num >= 5