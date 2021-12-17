from config.config import SNOWSQL_PW, SNOWSQL_USER, SNOWSQL_ACCOUNT
from utilities.LogHandler import get_logger
import snowflake.connector

# import logger
logger = get_logger(__name__)


def get_snowflake_connection():
    conn = snowflake.connector.connect(
        user=SNOWSQL_USER,
        password=SNOWSQL_PW,
        account=SNOWSQL_ACCOUNT
    )
    return conn


class SnowflakeClient:

    def __init__(self, warehouse, database, schema, table):
        logger.info("SnowflakeClient instance created")
        self.connection = get_snowflake_connection()
        self.cursor = self.get_cursor()
        self.warehouse = warehouse
        self.database = database
        self.schema = schema
        self.table = table
        self.cursor.execute(f"USE WAREHOUSE {self.warehouse}")
        self.cursor.execute(f"USE DATABASE {self.database}")
        # self.cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {self.schema}")
        # self.cursor.execute(f"USE TABLE {table}")

    def get_cursor(self):
        cursor = self.connection.cursor()
        return cursor

    def get_warehouse(self):
        return self.warehouse

    def set_warehouse(self, warehouse):
        self.warehouse = warehouse

    def get_database(self):
        return self.database

    def set_database(self, database):
        self.database = database

    def execute_query(self, query):
        self.cursor.execute(query)
        one_row = self.cursor.fetchone()
        print(one_row[0])

    def close_connection(self):
        self.cursor.close()
