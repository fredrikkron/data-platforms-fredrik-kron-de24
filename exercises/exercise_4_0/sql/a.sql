SELECT
    utbildningsnamn,
    "utbildningsanordnare administrativ enhet" AS school
INTO 
    a
FROM
    myh_2024
WHERE
    LOWER(utbildningsnamn) LIKE 'data eng%'