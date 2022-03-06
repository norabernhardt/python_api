from urllib import response
import boto3
import logging
from botocore.exceptions import ClientError
import os
#EASIER VERSION COULD BE:
# def create_bucket(bucket_name, client):
#     response=client.create_bucket(
#         Bucket=bucket_name)
#     print(response)
# def upload_json_to_s3(bucket_name, file_name, data):
#     client.upload_file(data, bucket_name, file_name)


def create_bucket(bucket_name, region=None):
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            s3_client.create_bucket(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
create_bucket("the-covid-showroom-220304", "us-east-1")

def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
upload_file("corona-data.json", "the-covid-showroom-220304")