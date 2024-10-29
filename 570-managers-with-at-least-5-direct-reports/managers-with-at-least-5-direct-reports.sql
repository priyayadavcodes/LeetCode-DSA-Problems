with tab as (select managerID,
count(managerId) as num 
from employee
group by managerID)

select name
from employee
where id in (select managerId
            from tab 
            where num >=5)