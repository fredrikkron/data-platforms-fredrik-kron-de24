SELECT
    utbildningsnamn,
    "utbildningsanordnare administrativ enhet" AS skola,
    beslut INTO b
FROM
    myh_2024
WHERE
    LOWER(utbildningsnamn) LIKE 'data eng%'
    AND LOWER(beslut) LIKE 'beviljad';