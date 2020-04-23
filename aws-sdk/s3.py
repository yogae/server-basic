import boto3 as aws
import botostubs

s3 = aws.client('s3') # type: botostubs.S3


def print_bucket_name():
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        print(bucket['Name'])

# print_bucket_name()


def get_bucket_name(num):
    response = s3.list_buckets()
    return response['Buckets'][num]['Name']


def list_objects(bucket_name):
    list_objects = s3.list_objects_v2(Bucket=bucket_name)
    for obj in list_objects['Contents']:
        print(obj['Key'])


bucket_name = get_bucket_name(0)
list_objects(bucket_name)
