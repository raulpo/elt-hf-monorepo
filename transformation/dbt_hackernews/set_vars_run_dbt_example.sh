export PG_HOST=hostname
export PG_PORT=port
export PG_USERNAME=postgres_username
export PG_PASSWORD=postgres_password
export PG_DATABASE=postgres_database
export PG_SCHEMA_RAW=postgres_schema_raw
export PG_SCHEMA_FINAL=postgres_schema_final

uv run dbt run --profiles-dir ./ --select 'hacker_news_subset'
