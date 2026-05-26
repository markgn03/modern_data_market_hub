with raw_transactions as (
    select
        1 as transaction_id,
        '2026-05-26' as transaction_date,
        'EUR' as currency,
        150.00 as gross_amount,
        'Desktop' as device_type
    union all
    select
        2 as transaction_id,
        '2026-05-26' as transaction_date,
        'USD' as currency,
        200.00 as gross_amount,
        'Mobile' as device_type
)

select
    transaction_id,
    cast(transaction_date as date) as transaction_date,
    upper(currency) as currency,
    cast(gross_amount as double) as gross_amount,
    lower(device_type) as device_type
from raw_transactions