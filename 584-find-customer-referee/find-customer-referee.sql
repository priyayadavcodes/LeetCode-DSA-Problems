
select name from
customer
where id not in (SELECT id 
                FROM Customer
                 WHERE referee_id =  2
                ) 

