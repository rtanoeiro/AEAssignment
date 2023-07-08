from clients.data_lake import connect_data_lake
import pandas as pd
import os
from config.config import user, password, host, database 

def query_data_lake(query):
  """Queries data in postgresql"""
  engine = connect_data_lake(user,password,host,database)
  data_df = pd.read_sql(query, engine)
  return data_df

def generate_report(report_details, working_dir):
  """Generates report on queried data in a CSV file"""
  report_dept = report_details['department']
  report_query = report_details['query']
  
  report_data = query_data_lake(report_query)
  report_filepath = os.path.join(working_dir,f'{report_dept}_report.csv')
  report_data.to_csv(report_filepath)
  
  print(f"{report_dept.capitalize()} report saved to {report_filepath}. The report contains {len(report_data)} rows.")
  return report_filepath, report_dept

def generate_all_reports(reports_list, working_dir):
  """Generates reports for all departments"""
  report_filepaths_dict = {}
  for report in reports_list:
    filepath, dept = generate_report(report, working_dir)
    report_filepaths_dict[dept] = filepath
  return report_filepaths_dict
