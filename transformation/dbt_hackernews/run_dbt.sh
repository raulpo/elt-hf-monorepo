uv run dbt run --profiles-dir ./ --select 'hacker_news_subset'
uv run dbt test --profiles-dir ./ --select 'hacker_news_subset'