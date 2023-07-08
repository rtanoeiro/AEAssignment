import pandas as pd

def read_data(data_filepath):
  """Reads data into dataframe"""
  data = pd.read_csv(data_filepath)
  return data

def fill_customer_country(data):
  """Fills customer and country data"""
  return data

def fill_gender(data):
  """Fills gender data"""
  return data
  
def apply_transformations(extracted_data_filepath):
  """Applies all transformations to extracted data"""
  try:
    extracted_data = read_data(extracted_data_filepath)
    transformed_data = fill_customer_country(extracted_data)
    transformed_data = fill_gender(transformed_data)
    print('Applied transformations to data')
    return transformed_data
  except Exception as e:
    print(f'Error occured while transforming data: {e}')