#AWS Lambda Volume Type Modifier
Overview
The AWS Lambda Volume Type Modifier is a serverless application that automatically modifies newly created Elastic Block Store (EBS) volumes to use the gp3 volume type. This Lambda function is triggered by a CloudWatch Event Rule that captures EBS Volume Notification events.

The Lambda function checks if the newly created volume is already of type gp3. If not, it modifies the volume type to gp3 using the AWS EC2 API.

Prerequisites
Before setting up the AWS Lambda Volume Type Modifier, make sure you have the following prerequisites:

An AWS account with the necessary permissions to create and configure Lambda functions, CloudWatch Event Rules, and modify EC2 volumes.
AWS CLI installed and configured with access to the desired AWS account.
