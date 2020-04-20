import boto3 as aws

client = aws.client('s3')

def get_bucket_name(num):
    response = client.list_buckets()
    return response['Buckets'][num]['Name']

def list_objects(bucket_name):
    key_list=[]
    list_objects = client.list_objects_v2(Bucket=bucket_name)
    if list_objects['KeyCount'] == 0: return []
    for obj in list_objects['Contents']:
        key_list.append(obj['Key'])
    return key_list

def delete_objects(bucket_name, object_key_list):
    if len(object_key_list) != 0:
        delete_object={
           'Objects': []
        }
        for key in object_key_list:
            delete_object['Objects'].append({ 'Key': key })
        client.delete_objects(
            Bucket=bucket_name,
            Delete=delete_object
        )
        return True
    else:
        return False
bucket_name = get_bucket_name(0)
object_key_list = list_objects(bucket_name)
deleted = delete_objects(bucket_name, object_key_list)

if deleted: 
    print('bucket: {}, keys: {}'.format(bucket_name, object_key_list))
else:
    print('bucket: {}, empty bucket'.format(bucket_name))
        



