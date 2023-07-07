from clients.s3 import access_s3

def download_file(s3_client, bucket_name, s3_file_path, s3_download_file_path):
  s3_client.download_file(Bucket=bucket_name, Key=s3_file_path, Filename=s3_download_file_path)