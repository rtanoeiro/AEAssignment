import boto3
from config.dev import bucket_name


def get_daily_data(download_from, download_to):
    """
    Get daily data from S3 bucket
    """
    s3_resource = boto3.resource("s3")

    s3_resource.meta.client.download_file(
        Bucket=bucket_name, Key=download_from, Filename=download_to
    )


def upload_reports(upload_from, upload_to):
    """
    Upload reports to S3 bucket
    """
    s3_resource = boto3.resource("s3")

    s3_resource.meta.client.upload_file(
        Bucket=bucket_name, Filename=upload_from, Key=upload_to
    )
