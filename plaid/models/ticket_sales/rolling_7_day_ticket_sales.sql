{{
    config(
        materialized="table"
    )
}}

SELECT
    DATE_TRUNC('day', b.book_date) AS sale_date,
    COUNT(*) AS total_tickets_sold_rolling_7_days
FROM
    {{ source('bookings', 'bookings') }} b
        JOIN
    {{ source('bookings', 'tickets') }} t ON b.book_ref = t.book_ref
WHERE
        b.book_date >= CURRENT_DATE - INTERVAL '6 days'
GROUP BY
    sale_date