-- select 
-- query_name,
-- Round(sum(rating/position),2) as quality,
-- Round((1/rating)*100,2) as poor_query_percentage
-- from queries 
-- where rating < 3
-- group by query_name


SELECT 
    query_name,
    ROUND(avg(rating / position), 2) AS quality,
    ROUND(100.0 * SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) / COUNT(*), 2) AS poor_query_percentage
FROM 
    queries
where query_name is not null
GROUP BY 
    query_name

