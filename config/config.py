import logging
import os
import pathlib
from logging.handlers import RotatingFileHandler

# APP Constants
BASE_DIR = str(pathlib.Path(__file__).parent.parent.resolve())

SNOWSQL_PW = <SNOWFLAKE PW>
SNOWSQL_USER = <SNOWFLAKE USERNAME>
SNOWSQL_ACCOUNT = <SNOWFLAKE ACCOUNT> #EX: 'XXXXXXX.us-east-2.aws'

SNOW_WAREHOUSE = <WAREHOUSE NAME>
SNOW_DATABASE = <DB NAME>
SNOW_SCHEMA = <SCHEMA NAME>
SNOW_TABLE = <TABLE NAME AND INFO> #ex: 'test_table(col1 int, col2 string, col3 string, col4 string, col5 string, col6 string, col7 string, col8 string, col9 string, col10 string)'
SNOW_FILE_FORMAT = <FILE FORMAT NAME>
