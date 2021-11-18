-- inner join
SELECT c.name as genre, COUNT(*) as number_of_shows
FROM tv_shows a
INNER JOIN tv_show_genres b
ON a.id = b.show_id
INNER JOIN tv_genres c
ON b.genre_id = c.id
GROUP BY c.name
ORDER BY 2 DESC;
