with raw_rates as (
    select '2026-05-26' as rate_date, 'EUR' as currency, 1.00 as exchange_rate
    union all
    select '2026-05-26' as rate_date, 'USD' as currency, 0.92 as exchange_rate
)

select
    cast(rate_date as date) as rate_date,
    upper(currency) as currency,
    cast(exchange_rate as double) as exchange_rate
from raw_rates