WITH RECURSIVE FlightSegments AS (
    SELECT
        departure_airport AS origin_airport,
        departure_airport AS transfer_airport,
        arrival_airport AS destination_airport,
        scheduled_departure AS departure_time,
        scheduled_arrival AS arrival_time,
        ARRAY[flight_no::bpchar] AS flight_numbers,
        duration AS total_duration,
        0 AS num_stops
    FROM
        {{ source('bookings', 'routes') }}
    UNION ALL
    SELECT
        fs.origin_airport,
        r.departure_airport AS transfer_airport,
        r.arrival_airport AS destination_airport,
        fs.departure_time AS departure_time,
        r.scheduled_arrival AS arrival_time,
        fs.flight_numbers || r.flight_no::bpchar AS flight_numbers,
                fs.total_duration + r.duration +
                CASE
                    WHEN r.scheduled_departure > fs.arrival_time THEN r.scheduled_departure - fs.arrival_time
                    ELSE interval '24 hours' + r.scheduled_departure - fs.arrival_time
                END
                AS total_duration,
        fs.num_stops + 1 AS num_stops
    FROM
        FlightSegments fs
    JOIN
        {{ source('bookings', 'routes') }} r ON fs.destination_airport = r.departure_airport
    WHERE
    fs.num_stops < 3
    )
SELECT
    origin_airport as origin_airport_code,
    destination_airport as destination_airport_code,
    flight_numbers,
    num_stops,
    total_duration,
    transfer_airport as transfer_airport_code,
    departure_time,
    arrival_time
FROM
    FlightSegments
WHERE
        num_stops <= 1 AND total_duration <= interval '24 hours' AND origin_airport != destination_airport
ORDER BY
    num_stops, total_duration
