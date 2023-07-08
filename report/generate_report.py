# from .base_queries import FINANCE_QUERY, MARKETING_QUERY
from clients.data_lake import connect_data_lake
import pandas as pd
import os

def query_data_lake(query, working_dir):
  engine = connect_data_lake()
  data_df = pd.read_sql(query, engine)
  return data_df
  
def generate_finance_reports(finance_query, working_dir):
  finance_report = query_data_lake(finance_query, working_dir)
  finance_report_path = os.path.join(working_dir, 'finance_report.csv')
  finance_report.to_csv(finance_report_path)
  
  print(
        f"Finance report saved to {finance_report_path}. The report contains {len(finance_report)} rows."
    )
  
def generate_marketing_reports(marketing_query, working_dir):
  marketing_report = query_data_lake(marketing_query, working_dir)
  marketing_report_path = os.path.join(working_dir, 'marketing_report.csv')
  marketing_report.to_csv(marketing_report_path)
  
  print(
        f"Marketing report saved to {marketing_report_path}. The report contains {len(marketing_report)} rows."
    )