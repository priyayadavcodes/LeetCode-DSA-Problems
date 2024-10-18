SELECT curr.id
FROM weather curr
LEFT JOIN weather prev
  ON curr.recorddate = DATE_ADD(prev.recorddate, INTERVAL 1 DAY)
WHERE prev.temperature IS NOT NULL
  AND curr.temperature > prev.temperature;
