SELECT curr.id
FROM weather curr
CROSS JOIN weather prev
WHERE DATEDIFF(curr.recorddate, prev.recorddate) = 1
  AND curr.temperature > prev.temperature;
