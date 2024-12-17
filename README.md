Here’s a detailed **README.md** for your project, explaining how to use the scripts (`send.py`, `read.py`, and `create_sns_sqs.py`), and setup the environment:

---

# SNS-SQS Integration

This project demonstrates the integration of **Amazon SNS (Simple Notification Service)** and **SQS (Simple Queue Service)** using the **AWS SDK for Python (Boto3)**. The scripts allow you to:

1. **Create an SNS Topic and SQS Queue**.
2. **Send messages** to the SNS topic.
3. **Read messages** from the SQS queue.

---

## Prerequisites

Before you start, ensure that:

1. **Python 3.7+** is installed.
2. **AWS CLI** is configured with valid AWS credentials (`aws configure`).
3. You have the necessary **permissions** to work with SNS and SQS on your AWS account.

---

## Project Structure

```
sns_sqs_integration/
│
├── send.py            # Script to send messages to SNS
├── read.py            # Script to read messages from SQS
├── create_sns_sqs.py  # Script to create SNS topic and SQS queue
├── requirements.txt   # List of required Python packages
└── README.md          # Project documentation
```

---

## Installation

1. **Clone the repository** or download the project files to your local machine.

2. **Install required dependencies**:
   Navigate to the project directory and run:
   ```bash
   pip install -r requirements.txt
   ```

---

## Setup

You need to set the AWS region before running the scripts. The default region is **us-east-1**, but you can change it by setting the `AWS_REGION` environment variable.

```bash
export AWS_REGION=us-east-1
```

---

## Usage

### 1. **Create SNS Topic, SQS Queue, and Subscription**

Run `create_sns_sqs.py` to create an SNS topic, an SQS queue, subscribe the SQS queue to the SNS topic, and set the appropriate permissions.

#### Command:
```bash
python create_sns_sqs.py
```

This will:
- Create an SNS Topic (`MySNSTopic`).
- Create an SQS Queue (`MySQSQueue`).
- Subscribe the SQS Queue to the SNS Topic.
- Set the necessary permissions for SNS to send messages to SQS.

---

### 2. **Send Messages to SNS**

After creating the resources, you can send messages to the SNS topic using the `send.py` script.

#### Command:
```bash
python send.py
```

This will send a predefined message to the SNS Topic you created earlier (`MySNSTopic`).

You can modify the message in the `send.py` script, as per your needs.

---

### 3. **Read Messages from SQS**

Once a message is published to SNS, it will be delivered to the SQS Queue. You can read the messages from the queue using the `read.py` script.

#### Command:
```bash
python read.py
```

This will:
- Fetch one message from the SQS queue (`MySQSQueue`).
- Display the message content.
- Delete the message from the queue after processing.

---

## Example Flow

1. **Run `create_sns_sqs.py`** to create SNS Topic and SQS Queue:
   ```bash
   python create_sns_sqs.py
   ```

2. **Send a message to the SNS topic** using `send.py`:
   ```bash
   python send.py
   ```

3. **Read the message** from the SQS queue using `read.py`:
   ```bash
   python read.py
   ```

---

## Environment Variables

You can set the AWS region for the scripts by setting the following environment variable:

```bash
export AWS_REGION=us-east-1
```

Alternatively, you can set the environment variable directly within the scripts if you want to hardcode the region.

---

## Requirements

The following packages are required to run the scripts:

1. **boto3**: AWS SDK for Python

Install the required dependencies via the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## Cleanup

After testing, you may want to delete the resources created (SNS Topic and SQS Queue). You can either do this manually through the AWS Console or use the AWS CLI.

For example, to delete the SQS queue:

```bash
aws sqs delete-queue --queue-url <queue-url>
```

To delete the SNS topic:

```bash
aws sns delete-topic --topic-arn <topic-arn>
```

---

## Troubleshooting

- Ensure that your AWS credentials are configured correctly with sufficient permissions to create and manage SNS and SQS resources.
- Verify that the **AWS region** is set properly by checking the `AWS_REGION` environment variable.
- If you are using a specific region, ensure that SNS and SQS are supported in that region.

---

## License

This project is licensed under the MIT License.

---

This **README.md** file provides complete instructions for setting up and using the project. It includes commands for creating resources, sending and reading messages, environment setup, and handling potential errors.

