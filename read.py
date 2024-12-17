import boto3
import os

# Get the region from an environment variable or set a default region
region = os.getenv('AWS_REGION', 'us-east-1')  # Default to 'us-east-1' if not set

# Initialize SQS client with the specified region
sqs = boto3.client('sqs', region_name=region)

# Initialize STS client to fetch account ID
sts = boto3.client('sts', region_name=region)

def get_account_id():
    """
    Get the AWS Account ID using the STS service
    """
    identity = sts.get_caller_identity()
    return identity['Account']

def receive_message_from_sqs(queue_url):
    """
    Receive a message from the SQS queue
    """
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1
    )
    return response.get('Messages', [])

def delete_message_from_sqs(queue_url, receipt_handle):
    """
    Delete a message from SQS queue
    """
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )
    print("Message deleted from SQS.")

if __name__ == '__main__':
    # Get the AWS Account ID dynamically
    account_id = get_account_id()
    print(f"AWS Account ID: {account_id}")

    # Construct SQS Queue URL using the account ID and region (optional)
    queue_url = f'https://sqs.{region}.amazonaws.com/{account_id}/MySQSQueue'
    
    # Receive message from SQS
    messages = receive_message_from_sqs(queue_url)

    if messages:
        for message in messages:
            print(f"Received message from SQS: {message['Body']}")

            # After processing the message, delete it from SQS
            delete_message_from_sqs(queue_url, message['ReceiptHandle'])
    else:
        print("No messages received from SQS.")
