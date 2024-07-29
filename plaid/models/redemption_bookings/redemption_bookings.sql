{{
    config(
        materialized="table"
    )
}}


SELECT
    DATE_TRUNC('day', book_date) AS booking_date,
    COUNT(*) AS redemption_bookings_count
FROM
    {{ source('bookings', 'bookings') }} b
WHERE
    b.total_amount in (99999999.00, 88888888.00, -12345678.00, -1.00, 0.00)
GROUP BY
    booking_date