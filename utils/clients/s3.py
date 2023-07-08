import boto3

def access_s3():
  """Create a connection to AWS S3"""
  return boto3.client("s3")