
from .logging_config import get_logger

logger = get_logger("utils")

def add_stg_prefix(query_dict: dict) -> dict:
    """
    Add stg_ prefix to table names
    """
    table_name = {}

    for key, value in query_dict.items():
        new_name = f"stg_{key}"
        table_name[new_name] = value

    logger.info("Added stg_ prefix to table names")
    return table_name
