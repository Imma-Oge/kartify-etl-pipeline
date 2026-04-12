from .logging_config import get_logger

logger = get_logger("load")

def load_to_snowflake(dataframes: dict, engine):
    """
    Load DataFrames into destination (example)
    """
    for table, df in dataframes.items():
        try:
            logger.info(f"Loading {table}")

            df.to_sql(table, engine, if_exists="replace", index=False)

            logger.info(f"Loaded {len(df)} rows into {table}")

        except Exception as e:
            logger.error(f"Failed to load {table}: {e}")
            raise
