import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL as sa_URL
from snowflake.sqlalchemy import URL

# The rest of your code...

load_dotenv()

# source credentials
def get_postgres_engine():
    url = sa_URL.create(
        drivername="postgresql+psycopg2",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", 5432)), # Default 5432 added for safety
        database=os.getenv("DB_NAME"),
        query={"sslmode": "require"}
    )
    return create_engine(url)

def get_snowflake_engine():
    url = URL(
        user=os.getenv("SF_USER"),
        password=os.getenv("SF_PASSWORD"),
        account=os.getenv("SF_ACCOUNT"),
        warehouse=os.getenv("SF_WH"),
        database=os.getenv("SF_DB"),
        schema=os.getenv("SF_SCHEMA")
    )
    return create_engine(url)



def get_snowflake_engine(schema_name="RAW"):
    url = URL(
        user=os.getenv("SF_USER"),
        # ... other variables stay same ...
        schema=os.getenv(schema_name) 
    )
    return create_engine(url)
