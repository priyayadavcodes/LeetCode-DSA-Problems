with tab as(select
num,
case 
    when count(num) = 1 then 1
    else 0
end as cnt 
from mynumbers
group by num )

select max(num) as num
from tab 
where cnt = 1