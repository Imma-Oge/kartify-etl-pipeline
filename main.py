from dotenv import load_dotenv
load_dotenv()
from data_pipeline.connections import get_postgres_engine
from data_pipeline.connections import get_snowflake_engine

from data_pipeline.queries import create_queries
from data_pipeline.utils import add_stg_prefix
from data_pipeline.extract import extract_data
from data_pipeline.logging_config import get_logger

logger = get_logger("main")

tables = [
    'categories',
    'products',
    'customers',
    'orders',
    'coupons',
    'order_items',
    'payments',
    'shipping',
    'inventory',
    'reviews'
]

def run_pipeline():
    try:
        logger.info("Starting ETL pipeline")

        # connection
        engine = get_postgres_engine()

        # build queries
        queries = create_queries(tables)

        # rename tables
        staged_queries = add_stg_prefix(queries)

        # extract
        dataframes = extract_data(staged_queries, engine)

        logger.info("ETL pipeline completed successfully")

        return dataframes

    except Exception as e:
        logger.critical(f"Pipeline failed: {e}")
        raise


if __name__ == "__main__":
    run_pipeline()