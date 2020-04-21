import boto3 as aws

# 사용법
client = aws.client('s3') 

# def print_bucket_name():
#     response = client.list_buckets()
#     for bucket in response['Buckets']:
#         print(bucket['Name'])

# print_bucket_name()

def get_bucket_name(num):
    response = client.list_buckets()
    return response['Buckets'][num]['Name']

def list_objects(bucket_name):
    list_objects = client.list_objects_v2(Bucket=bucket_name)
    print(list_objects['Contents'])
    for obj in list_objects['Contents']:
        print(obj['Key'])

bucket_name = get_bucket_name(0)
list_objects(bucket_name)
