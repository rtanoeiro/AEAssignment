import pandas as pd
from config.dev import datatypes

data = pd.read_csv("data/platform_transactions.csv")
print(datatypes.items())
columns_tuple = tuple(data.columns)
column_types = [f"{column_type}{column_type}" for column_type in datatypes.items()]
print(columns_tuple)


EVENTS = """
CREATE TABLE IF NOT EXISTS {table} (
{columns}
)

INSERT INTO {table} into {columns_tuple} VALUES {values_tuple

"""
