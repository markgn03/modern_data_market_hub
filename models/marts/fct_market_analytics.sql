with transactions as (
    select * from {{ ref('stg_market_transactions') }}
),

rates as (
    select * from {{ ref('stg_currency_rates') }}
),

enriched_transactions as (
    select
        t.transaction_id,
        t.transaction_date,
        t.currency,
        t.gross_amount,
        t.device_type,
        r.exchange_rate,
        cast(t.gross_amount * r.exchange_rate as double) as gross_amount_eur
    from transactions t
    left join rates r
        on t.transaction_date = r.rate_date
        and t.currency = r.currency
),

final_mart as (
    select
        *,
        case
            when gross_amount_eur >= 150.0 then 'high_value'
            else 'regular_value'
        end as transaction_category
    from enriched_transactions
)

select * from final_mart