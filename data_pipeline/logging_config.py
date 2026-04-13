
import logging
import os

# Ensure logs folder exists
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # default level (change to DEBUG when needed)
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/pipeline.log"),
        logging.StreamHandler()
    ]
)

def get_logger(name: str):
    """
    Returns a logger with a given name
    """
    return logging.getLogger(name)