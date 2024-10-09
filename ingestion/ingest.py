import duckdb

import airbyte as ab
from airbyte.caches import PostgresCache

from os import getenv
from dotenv import load_dotenv

load_dotenv()

hackernews_dataset = duckdb.sql("SELECT * FROM 'hf://datasets/Linkseed/hacker_news_with_comments/test.csv';").df().to_csv("hackernews_dataset.csv")

source: ab.Source = ab.get_source("source-file")

# Configure the source
source.set_config(
    config={
        "dataset_name": "raw_hacker_news_with_comments",
        "format": "csv",  # Adjust this to get a larger or smaller dataset
        "url": "hackernews_dataset.csv",
        "provider": { 
            "title" : "Local Filesystem (limited)",
            "storage": "local"
        },        
    },
)

# Verify the config and creds by running `check`:
source.check()


#Define a Postgres Cache and pass the necessary configuration
pg_cache = PostgresCache(    
      host=getenv('PG_HOST'),
      port=getenv('PG_PORT'),
      username=getenv('PG_USERNAME'),
      password=getenv('PG_PASSWORD'),
      database=getenv('PG_DATABASE'),
      schema_name=getenv('PG_SCHEMA_RAW')
)

# Select all of the source's streams and read data into the previously defined Postgres cache:
source.select_all_streams()

read_result: ab.ReadResult = source.read(cache=pg_cache)
