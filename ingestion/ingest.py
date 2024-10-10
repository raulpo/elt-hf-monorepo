import dlt
import duckdb


def run_ingestion():
    query = '''
        SELECT *
        FROM 'hf://datasets/Linkseed/hacker_news_with_comments/test.csv';
    '''
    df = duckdb.sql(query).to_arrow_table()

    pipeline = dlt.pipeline(
        pipeline_name="hackernews_pipeline",
        destination="postgres",
        dataset_name="raw"
    )

    pipeline.run(
        df,
        table_name="raw_hacker_news_with_comments",
        write_disposition="replace"
    )


if __name__ == "__main__":
    run_ingestion()
