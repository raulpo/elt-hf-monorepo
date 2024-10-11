with int_hacker_news as (
    select
        *
    from {{ source('postgres_data', 'raw_hacker_news_with_comments') }}
),

last_timestamp as (
    select 
        max(time_ts) - INTERVAL '3 months' as last_ts
    from
        int_hacker_news
)

select
    title as title,
    comment_author as comment_author,
    comment_text as comment_text,
    time_ts as time_ts
from
    int_hacker_news, last_timestamp
where
    time_ts >= last_timestamp.last_ts