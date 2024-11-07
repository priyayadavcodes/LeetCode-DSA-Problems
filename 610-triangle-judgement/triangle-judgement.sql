with tab as (select * , 
case 
    when x+y > z and y+z > x and x+z > y then 'Yes' 
    else 'No'
end as triangle
from 
triangle )

select 
* from tab 
