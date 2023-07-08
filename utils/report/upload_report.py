import datetime
from clients.s3 import access_s3


def upload_report_s3(bucket_name, reports_folder, folder_alias, report_filepath, department):
  """Uploads file on S3"""
  s3_client = access_s3()
  TODAY = datetime.datetime.now().strftime("%Y-%m-%d")
  s3_report_filepath = f"{reports_folder}/{folder_alias}/{department}_report_{TODAY}.csv",
  s3_client.upload_file(
        Bucket=bucket_name, Filename=report_filepath, Key=s3_report_filepath
    )

def upload_all_reports(report_filepaths_dict, bucket_name, reports_folder, folder_alias):
  """Uploads all saved reports of departments on S3"""
  for dept, filepath in report_filepaths_dict.items():
    upload_report_s3(bucket_name,reports_folder, folder_alias, filepath, dept)
    
    
    
  
  