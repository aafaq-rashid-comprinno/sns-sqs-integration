import boto3
import json
import os

# Get the region from an environment variable or set a default region
region = os.getenv('AWS_REGION', 'us-east-1')  # Replace 'us-east-1' with your default region if needed

# Initialize clients for SNS and SQS with the specified region
sns = boto3.client('sns', region_name=region)
sqs = boto3.client('sqs', region_name=region)

def create_sns_topic(topic_name):
    """
    Create an SNS topic and return the Topic ARN
    """
    response = sns.create_topic(Name=topic_name)
    return response['TopicArn']

def create_sqs_queue(queue_name):
    """
    Create an SQS queue and return the Queue URL
    """
    response = sqs.create_queue(QueueName=queue_name)
    return response['QueueUrl']

def get_queue_arn(queue_url):
    """
    Get the ARN of the SQS queue
    """
    response = sqs.get_queue_attributes(
        QueueUrl=queue_url, AttributeNames=['QueueArn']
    )
    return response['Attributes']['QueueArn']

def subscribe_sqs_to_sns(topic_arn, queue_arn):
    """
    Subscribe the SQS queue to the SNS topic
    """
    sns.subscribe(
        TopicArn=topic_arn,
        Protocol='sqs',
        Endpoint=queue_arn
    )
    print(f"SQS Queue subscribed to SNS Topic {topic_arn}.")

def set_sqs_permissions(queue_url, topic_arn, queue_arn):
    """
    Set the necessary permissions on the SQS queue to allow SNS to send messages
    """
    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {"Service": "sns.amazonaws.com"},
                "Action": "sqs:SendMessage",
                "Resource": queue_arn,
                "Condition": {"ArnEquals": {"aws:SourceArn": topic_arn}}
            }
        ]
    }
    sqs.set_queue_attributes(
        QueueUrl=queue_url,
        Attributes={"Policy": json.dumps(policy)}
    )
    print(f"Permissions set for SNS to send messages to SQS.")

def main():
    # Specify the names for SNS Topic and SQS Queue
    topic_name = 'MySNSTopic'
    queue_name = 'MySQSQueue'

    # Step 1: Create SNS Topic
    topic_arn = create_sns_topic(topic_name)
    print(f"SNS Topic created with ARN: {topic_arn}")

    # Step 2: Create SQS Queue
    queue_url = create_sqs_queue(queue_name)
    print(f"SQS Queue created with URL: {queue_url}")

    # Step 3: Get the ARN of the SQS Queue
    queue_arn = get_queue_arn(queue_url)
    print(f"SQS Queue ARN: {queue_arn}")

    # Step 4: Subscribe the SQS Queue to the SNS Topic
    subscribe_sqs_to_sns(topic_arn, queue_arn)

    # Step 5: Set Permissions on SQS for SNS
    set_sqs_permissions(queue_url, topic_arn, queue_arn)

if __name__ == '__main__':
    main()
