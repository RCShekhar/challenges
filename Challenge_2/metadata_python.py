# Sample for blob object metadata
from google.cloud import storage

def object_metadata(bucket_name: str, object_name: str)-> str:
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    obj = bucket.blob(object_name)
    result = '{'
    result += f'name:{obj.name}'
    result += f'bucket:{obj.bucket}'
    result += f'size:{obj.size}'
    result += '}'

meta = object_metadata('argiculture-in-india-data', '9ef84268-d588-465a-a308-a864a43d0070_20220816.csv')
print(meta)