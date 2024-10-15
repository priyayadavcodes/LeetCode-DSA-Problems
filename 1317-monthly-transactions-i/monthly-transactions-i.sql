with t AS (
    SELECT *, DATE_FORMAT(trans_date, '%Y-%m') AS month 
    FROM transactions
)

select month, 
country, 
Count(state) as trans_count,
sum(Case
        when state = 'approved' then 1
        else 0
        end) as approved_count,

Sum(amount) as trans_total_amount,

sum(Case
        when state = 'approved' then amount
        else 0
        end) as approved_total_amount
from t
group by t.month,country

