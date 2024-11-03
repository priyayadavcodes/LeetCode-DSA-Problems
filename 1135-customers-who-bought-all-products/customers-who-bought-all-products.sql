select 
customer_id
from 
customer 
where product_key in (select *
                      from product)
group by customer_id 
having count(distinct(product_key)) = (select count(product_key) 
                                        from 
                                        product)