from clients.s3 import access_s3

def download_file(bucket_name, s3_file_path, s3_download_file_path):
  """Downloads file from S3"""
  s3_client = access_s3()
  s3_client.download_file(Bucket=bucket_name, Key=s3_file_path, Filename=s3_download_file_path)