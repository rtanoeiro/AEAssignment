from config.config import bucket_name, data_folder
from clients.s3 import access_s3
from extract.get_s3_data import download_file
import os

s3_file_name = 'platform_transactions.csv'
s3_file_path = f'{data_folder}/{s3_file_name}'
working_dir = os.getcwd()
s3_download_file_path = os.path.join(working_dir, s3_file_name)

def main():
  s3_client = access_s3()
  download_file(s3_client, bucket_name, s3_file_path,s3_download_file_path)
  
if __name__ == "__main__":
    main()