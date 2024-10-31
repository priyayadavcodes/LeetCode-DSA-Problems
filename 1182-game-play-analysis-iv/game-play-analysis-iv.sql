WITH first_login AS (
    SELECT 
        player_id,
        MIN(event_date) AS first_login_date
    FROM 
        activity
    GROUP BY 
        player_id
),
next_day_login AS (
    SELECT 
        a.player_id,
        a.event_date,
        f.first_login_date
    FROM 
        activity a
    JOIN 
        first_login f ON a.player_id = f.player_id
    WHERE 
        DATEDIFF(a.event_date, f.first_login_date) = 1
)

SELECT 
    ROUND(COUNT(DISTINCT next_day_login.player_id) * 1.0 / COUNT(DISTINCT first_login.player_id), 2) AS fraction
FROM 
    first_login
LEFT JOIN 
    next_day_login ON first_login.player_id = next_day_login.player_id;
