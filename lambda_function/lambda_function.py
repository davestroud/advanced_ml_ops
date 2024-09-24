import boto3
import requests
from datetime import datetime

s3 = boto3.client('s3')

def lambda_handler(event, context):
    dataset_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
    s3_bucket = 'advanced-ml-operations'
    current_date = datetime.now().strftime('%Y-%m-%d')
    s3_key = f'covid19-data/confirmed_cases_{current_date}.csv'
    
    response = requests.get(dataset_url)
    if response.status_code == 200:
        s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=response.content)
        return {
            'statusCode': 200,
            'body': f'Successfully uploaded data for {current_date} to {s3_key}'
        }
    else:
        return {
            'statusCode': response.status_code,
            'body': f'Failed to fetch data from {dataset_url}'
        }
