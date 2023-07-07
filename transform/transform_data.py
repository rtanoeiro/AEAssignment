import pandas as pd

def read_data(data_filepath):
  data = pd.read_csv(data_filepath)
  return data

def apply_transformations(extracted_data):
  data_df = read_data(extracted_data)
  transformed_data_df1 = fill_customer_country(data_df)
  transformed_data_df2 = fill_gender(transformed_data_df1)
  return transformed_data_df2 
  
def fill_customer_country(data):
    return data

def fill_gender(data):
    return data
