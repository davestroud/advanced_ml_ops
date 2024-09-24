import boto3
import pandas as pd
import io

# Initialize S3 client
s3 = boto3.client('s3')

S3_BUCKET = 'advanced-ml-operations'
S3_KEY = 'covid19-data/confirmed_cases_2024-09-09.csv'

# Test the extract function
def test_extract():
    try:
        response = s3.get_object(Bucket=S3_BUCKET, Key=S3_KEY)
        status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")
        if status == 200:
            print("Successfully retrieved data from S3")
            data = pd.read_csv(io.BytesIO(response['Body'].read()))
            print(data.head())
        else:
            print(f"Failed to retrieve data from S3: {status}")
    except Exception as e:
        print(f"Error: {e}")

test_extract()
