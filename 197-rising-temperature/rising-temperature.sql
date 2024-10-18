select id from 
(select *,
lag(temperature
) over() as prev_temp,
lag(recorddate) over() as prev_date
from weather
order by recorddate) t 
where t.temperature > t.prev_temp  and datediff(recorddate,prev_date) = 1


