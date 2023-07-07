from config.config import bucket_name, data_folder
import os

s3_file_name = 'platform_transactions.csv'
s3_file_path = f'{data_folder}/{s3_file_name}'
working_dir = os.getcwd()
s3_download_file_path = os.path.join(working_dir, s3_file_name)