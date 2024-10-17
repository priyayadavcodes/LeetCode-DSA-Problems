select contest_id,
Round(100*(count(user_id)/(select count(user_id) as num from users)),2) as percentage
from register 
group by contest_id 
order by percentage desc , contest_id;
