import boto3
import json

print('Loading function')

def lambda_handler(event, context):
    payload = json.dumps(event, indent=2)
    print('Received event: ' +payload)
    result = "hello world, this is a terraform run api by richie"
    return {
        'statusCode' : 200,
        'body': result
    }