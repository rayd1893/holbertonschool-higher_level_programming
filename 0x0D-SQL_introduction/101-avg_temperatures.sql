-- Sort and group
SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY 2 DESC;
