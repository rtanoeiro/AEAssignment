from clients.data_lake import connect_data_lake
import pandas as pd

def load_data(transformed_data, host, database, user, password, table_name):
  engine = connect_data_lake(user, password, host, database)
  transformed_data.to_sql(table_name, engine, if_exists="append", index=False)
  print(f"Data saved to {table_name}. The table contains {len(transformed_data)} rows.")
  engine.dispose()