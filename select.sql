SELECT
    player_id,
    player_registration,
    player_seconds_online,
    region,
    payment_gw,
    description,
    is_package,
    package_id,
    round(money / exchange_rate.get_exchange_rate(currency, STR_TO_DATE(DATE_FORMAT(date_end,'%Y-%m-01 00:00:00'), '%Y-%m-%d %H:%i:%s')), 1) as money,
    currency,
    date_start,
    date_end,
    is_successful,
    is_refunded
FROM player_orders
WHERE date_start BETWEEN '2023-09-01' AND '2023-11-30'