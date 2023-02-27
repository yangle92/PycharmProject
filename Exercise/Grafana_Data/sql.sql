SELECT
  time AS "time",
  id
FROM Grafana_Data
WHERE
  $__timeFilter(time)
ORDER BY time