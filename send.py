import boto3
import os

# Get the region from an environment variable or set a default region
region = os.getenv('AWS_REGION', 'us-east-1')  # Default to 'us-east-1' if not set

# Initialize SNS client with the specified region
sns = boto3.client('sns', region_name=region)

# Initialize STS client to fetch account ID
sts = boto3.client('sts', region_name=region)

def get_account_id():
    """
    Get the AWS Account ID using the STS service
    """
    identity = sts.get_caller_identity()
    return identity['Account']

def send_message_to_sns(topic_arn, message):
    """
    Send a message to the SNS topic
    """
    sns.publish(
        TopicArn=topic_arn,
        Message=message
    )
    print(f"Message sent to SNS topic: {message}")

if __name__ == '__main__':
    # Get the AWS Account ID dynamically
    account_id = get_account_id()
    print(f"AWS Account ID: {account_id}")

    # Construct SNS Topic ARN using the account ID and region
    topic_arn = f'arn:aws:sns:{region}:{account_id}:MySNSTopic'
    
    # Message to send
    message = "This is a test message from SNS."

    # Send message to SNS
    send_message_to_sns(topic_arn, message)
