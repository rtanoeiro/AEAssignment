import pandas as pd

def read_data(data_filepath):
  data = pd.read_csv(data_filepath)
  return data

def fill_customer_country(data):
    return data

def fill_gender(data):
    return data
  
def apply_transformations(extracted_data_filepath):
  extracted_data = read_data(extracted_data_filepath)
  transformed_data = fill_customer_country(extracted_data)
  transformed_data = fill_gender(transformed_data)
  return transformed_data
