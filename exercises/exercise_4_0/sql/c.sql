SELECT
    utbildningsområde,
    COUNT(*) AS approved
INTO c
FROM
    myh_2024
WHERE
    LOWER(beslut) = 'beviljad'
GROUP BY utbildningsområde
ORDER BY approved DESC;