from urllib import response
import boto3

client=boto3.client("s3")
response=client.create_bucket(
    Bucket="the-covid-showroom-220304")
