SELECT curr.id
FROM weather curr
JOIN weather prev
  ON curr.recorddate = DATE_ADD(prev.recorddate, INTERVAL 1 DAY)
WHERE curr.temperature > prev.temperature;
