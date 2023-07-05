from base_queries import EVENTS
import pandas as pd
from sqlalchemy import create_engine
from config.dev import host, database, user, password, table_name

connection_string = f"postgresql://{user}:{password}@{host}/{database}"
engine = create_engine(connection_string)

data = pd.read_csv("data/platform_transactions.csv")
data.to_sql(table_name, engine, if_exists="append", index=False)

engine.dispose()
