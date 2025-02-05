SELECT
    utbildningsområde,
    COUNT(*) AS antal_beviljade
INTO c
FROM
    myh_2024
WHERE
    LOWER(beslut) = 'beviljad'
GROUP BY utbildningsområde
ORDER BY antal_beviljade DESC;