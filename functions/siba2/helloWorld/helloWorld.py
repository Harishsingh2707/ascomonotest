import json

def lambda_handler(event, context):
    print('event:',event)
    return {
        'statusCode': 200,
        'body': json.dumps("Hello from ASCO!!")
    }
