{{
    config(
        materialized="table"
    )
}}

SELECT
    DATE_TRUNC('day', b.book_date) AS sale_date,
    COUNT(*) AS total_tickets_sold
FROM
    {{ source('bookings', 'bookings') }} b
JOIN
    {{ source('bookings', 'tickets') }} t ON b.book_ref = t.book_ref
GROUP BY
    sale_date