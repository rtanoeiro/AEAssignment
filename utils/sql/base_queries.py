from config.config import database, table_name
from func import define_columns, join_columns, month_period


# CREATE TABLE AND INSERT DATA
column_definition = define_columns()
column_tuple = join_columns()
EVENTS = f"""
CREATE TABLE IF NOT EXISTS {database}.{table_name} (
{column_definition}
)

INSERT INTO {database}.{table_name} ({column_tuple})
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# QUERY DATA FOR REPORTING DEPARTMENT

month_beggining, month_end = month_period()

# Finance
FINANCE_QUERY = f"""
WITH TRANSACTIONS AS (
    SELECT * FROM {database}.{table_name}
)

SELECT
    CUSTOMER_COUNTRY,
    SUM(PRODUCT_VALUE) AS TOTAL_VALUE
FROM TRANSACTIONS
WHERE TRANSACTION_DATE BETWEEN {month_beggining} AND {month_end}
"""


# Marketing
MARKETING_QUERY = f"""
WITH TRANSACTIONS AS (
    SELECT * FROM {database}.{table_name}
)

SELECT
    CUSTOMER_COUNTRY,
    COUNT(ID) AS TOTAL_TRANSACTIONS
FROM TRANSACTIONS
WHERE TRANSACTION_DATE BETWEEN {month_beggining} AND {month_end}
"""
