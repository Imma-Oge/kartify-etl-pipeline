from .logging_config import get_logger

logger = get_logger("queries")

def create_queries(tables: list) -> dict:
    """
    Create SQL queries for each table
    """
    query = {}

    for t in tables:
        query[t] = f"SELECT * FROM {t}"

    logger.info(f"Created queries for {len(tables)} tables")
    return query
