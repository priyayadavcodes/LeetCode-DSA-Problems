with tab as (select s.user_id,
count(action) total_applied,
sum(case 
            when c.action = 'confirmed' then 1
            when c.action is null then 0
            else 0
    end) as status
from signups s
left join confirmations c
on c.user_id = s.user_id
group by s.user_id )

SELECT 
    user_id,
    CASE 
        WHEN total_applied = 0 THEN 0
        ELSE ROUND(status / total_applied, 2)
    END AS confirmation_rate
FROM tab;
