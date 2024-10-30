with tab as (select p.product_id,
sum(case 
    when u.purchase_date between p.start_date and p.end_date then u.units * p.price
    else 0
    end )as total_price,
sum(
    case 
    when u.purchase_date between p.start_date and p.end_date then u.units 
    when u.purchase_date is null then 1
    end ) as total_units
from prices p
left join unitssold u
on p.product_id = u.product_id
group by p.product_id)

select 
product_id,
round(total_price/total_units,2) as average_price
from tab 


