WITH tab AS (
    SELECT *
    FROM students s1
    CROSS JOIN subjects
)

SELECT 
    t.student_id,
    t.student_name,
    t.subject_name,
    COUNT(
        CASE 
            WHEN e.subject_name IS NOT NULL THEN 1 
            ELSE NULL
        END
    ) AS attended_exams
FROM tab t
LEFT JOIN examinations e 
    ON t.student_id = e.student_id AND t.subject_name = e.subject_name
GROUP BY t.student_id, t.student_name, t.subject_name
ORDER BY t.student_id, t.subject_name, attended_exams DESC;
