import pandas as pd
from .logging_config import get_logger

logger = get_logger("extract")

def extract_data(table_queries: dict, engine) -> dict:
    """
    Extract data from database into pandas DataFrames
    """
    dataframes = {}

    for table, query in table_queries.items():
        try:
            logger.info(f"Extracting {table}")
            
            df = pd.read_sql(query, engine)

            dataframes[table] = df

            logger.info(f"Extracted {len(df)} rows from {table}")

        except Exception as e:
            logger.error(f"Failed to extract {table}: {e}")
            raise

    return dataframes
