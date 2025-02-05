WITH
    myh_2024 AS (
        SELECT
            utbildningsområde,
            SUM(
                CASE
                    WHEN LOWER(beslut) = 'beviljad' THEN 1
                    ELSE 0
                END
            ) AS amount_of_approved,
            COUNT(*) as total_count
        FROM
            myh_2024
        GROUP BY
            utbildningsområde
    )
SELECT
    utbildningsområde,
    amount_of_approved,
    total_count,
    (amount_of_approved * 100 / total_count) AS percentage_of_approved INTO e
FROM
    myh_2024;