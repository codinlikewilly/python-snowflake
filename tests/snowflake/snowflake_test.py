#!/usr/bin/env python
from classes.snowflake.SnowflakeClient import get_snowflake_connection


# Gets the version
def test_snowflake_connection():
    ctx = get_snowflake_connection()
    cs = ctx.cursor()
    try:
        cs.execute("SELECT current_version()")
        one_row = cs.fetchone()
        print(one_row)
        assert (one_row is not None)
    finally:
        cs.close()
    ctx.close()
