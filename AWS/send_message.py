import json
import boto3

def lambda_handler(event, context):
    client = boto3.client("sqs")
    
    ip = event['requestContext']['identity']['sourceIp']
    request_time = event['requestContext']['requestTime']
    sqs_url = "https://sqs.ap-northeast-2.amazonaws.com/703474273090/load-test"
    
    response = client.send_message(
        QueueUrl = sqs_url,
        MessageBody = json.dumps((ip, request_time))
    )
            
    return {
        'statusCode': response["ResponseMetadata"]["HTTPStatusCode"],
        'body': json.dumps(response['ResponseMetadata']['HTTPStatusCode'])
    }
