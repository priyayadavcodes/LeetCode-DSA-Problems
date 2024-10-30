with tab as(select *,
case 
    when order_date = customer_pref_delivery_date then 'immediate'
    else 'scheduled'
end status,
ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS row_num
from delivery)


select 
Round(100 * avg(case
        when status = 'scheduled' then 0
        when status = 'immediate' then 1
    end),2) as immediate_percentage
from tab 
where row_num = 1
order by customer_id, order_date, customer_pref_delivery_date

