import boto3 as aws

client = aws.client('s3')

def get_bucket_name(num):
    response = client.list_buckets()
    return response['Buckets'][num]['Name']

def put_object(bucket_name, body):
    client.put_object(
        Bucket=bucket_name,
        Body=body,
        Key="test.txt"
    )

bucket_name = get_bucket_name(0)
put_object(bucket_name, 'qweqwe')


