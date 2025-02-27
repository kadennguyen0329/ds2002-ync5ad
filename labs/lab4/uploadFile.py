#!/usr/bin/python3

import requests
import boto3

url = "https://m.media-amazon.com/images/M/MV5BMjRjN2IzMWQtY2RjOS00ZGFlLThiMWEtNjQ3YWJkOTczMzU0XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
local_file = "ChiikawaUsagiHachiware.jpg"
bucket_name = "ds2002-ync5ad"
object_name = "ChiikawaUsagiHachiware.jpg"
expiration = 604800

response = requests.get(url, allow_redirects=True)
with open(local_file, 'wb') as file:
    file.write(response.content)
print(f"File downloaded to {local_file}")

s3_client = boto3.client('s3')

s3_client.upload_file(local_file, bucket_name, object_name)
print(f"File uploaded to s3://{bucket_name}/{object_name}")

presigned_url = s3_client.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket_name, 'Key': object_name},
        ExpiresIn=expiration
    )
print(f"Presigned URL: {presigned_url}")
