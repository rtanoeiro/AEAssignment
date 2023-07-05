from base_queries import FINANCE_QUERY, MARKETING_QUERY
import pandas as pd
from sqlalchemy import create_engine
from config.dev import host, database, user, password, table_name

connection_string = f"postgresql://{user}:{password}@{host}/{database}"
engine = create_engine(connection_string)

finance_report = pd.read_sql(FINANCE_QUERY, engine).to_csv("data/finance_report.csv")
marketing_report = pd.read_sql(MARKETING_QUERY, engine).to_csv(
    "data/marketing_report.csv"
)
