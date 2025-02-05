SELECT
    kommun, COUNT(*) AS approved_per_municipality
INTO d
FROM
    myh_2024
WHERE LOWER(beslut) = 'beviljad'
GROUP BY kommun
ORDER BY approved_per_municipality DESC;