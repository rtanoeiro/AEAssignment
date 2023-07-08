from clients.data_lake import connect_data_lake
import pandas as pd
from config.config import user, password, host, database, table_name 

def load_data(transformed_data):
  """Loads transformed data to Postgresql database"""
  try:
    engine = connect_data_lake(user, password, host, database)
    transformed_data.to_sql(table_name, engine, if_exists="append", index=False)
    print(f"Data saved to {table_name}. The table contains {len(transformed_data)} rows.")
    engine.dispose()
  except Exception as e:
    print(f'Error occured while loading data to Postgresql database: {e}')