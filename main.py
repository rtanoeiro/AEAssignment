from config.config import bucket_name, data_folder, reports_folder, folder_alias
from utils.extract.get_s3_data import download_file
from utils.transform.transform_data import apply_transformations
from utils.load.load_data import load_data
from utils.report.generate_report import generate_all_reports
from utils.report.upload_report import upload_all_reports
from utils.report.reports import reports_list
import os

# Data source
s3_file_name = 'platform_transactions.csv'
# Data source filepath on S3
s3_file_path = f'{data_folder}/{s3_file_name}'
# Data source working directory
working_dir = os.path.join(os.getcwd(),'data')
# Data source filepath
s3_download_file_path = os.path.join(working_dir, s3_file_name)


def main():

# Extract S3 data
  download_file(bucket_name, s3_file_path, s3_download_file_path)

 # Transform data 
  transformed_data = apply_transformations(s3_download_file_path)
  
 # Load data to data lake
  load_data(transformed_data)
 
 # Generate reports for each department
  report_filepaths_dict = generate_all_reports(reports_list, working_dir)

# Upload reports to S3
  upload_all_reports(report_filepaths_dict, bucket_name, reports_folder, folder_alias)

if __name__ == "__main__":
    main()