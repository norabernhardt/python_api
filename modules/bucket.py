import boto3

def create_bucket(bucket_name, region=None):
    client = boto3.client("s3")
    client.create_bucket(
        Bucket="myautomatedcoronachecks040322")