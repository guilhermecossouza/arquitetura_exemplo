import json

def validate_user_credentials(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }