import boto3

def access_s3():
  return boto3.client("s3")