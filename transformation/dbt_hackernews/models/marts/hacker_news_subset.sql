with int_hacker_news as (
    select
        *
    from {{ source('postgres_data', 'raw_hacker_news_with_comments') }}
),

last_timestamp as (
    select 
        cast(max(time_ts) as date) - INTERVAL '3 months' as last_ts
    from
        int_hacker_news
)

select
    title as title,
    comment_author as comment_author,
    comment_text as comment_text,
    cast(time_ts as date) as time_ts
from
    int_hacker_news, last_timestamp
where
    cast(time_ts as date) >= last_timestamp.last_ts