from config.config import bucket_name, data_folder, host, database, user, password, table_name
from clients.data_lake import connect_data_lake
from extract.get_s3_data import download_file
from transform.transform_data import apply_transformations
import os

s3_file_name = 'platform_transactions.csv'
s3_file_path = f'{data_folder}/{s3_file_name}'
working_dir = os.path.join(os.getcwd(),'data')
s3_download_file_path = os.path.join(working_dir, s3_file_name)


def main():

# Extract S3 Data
  download_file(bucket_name, s3_file_path,s3_download_file_path)

 # Transform Data 
  
  transformed_data = apply_transformations(s3_download_file_path)
  
  
 # Load Data
  connect_data_lake(user,password,host,database)
 
 # Generate Reports
 

if __name__ == "__main__":
    main()