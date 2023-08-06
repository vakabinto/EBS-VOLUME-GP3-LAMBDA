import boto3

def lambda_handler(event, context):
    # Check if the event is from AWS CloudWatch Events
    if 'detail-type' not in event or event['detail-type'] != 'EBS Volume Notification':
        return {
            'statusCode': 200,
            'body': 'Not an EBS Volume Notification event. No action needed.'
        }

    # Extract the volume ID from the event
    volume_id = event['resources'][0].split('/')[-1]

    # Initialize the AWS EC2 client
    ec2 = boto3.client('ec2')

    try:
        # Describe the volume to get its details
        response = ec2.describe_volumes(VolumeIds=[volume_id])
        volume = response['Volumes'][0]

        # Check if the volume type is already gp3
        if volume['VolumeType'] == 'gp3':
            print(f"Volume {volume_id} is already in gp3. No action needed.")
        else:
            # Modify the volume to gp3
            ec2.modify_volume(
                VolumeId=volume_id,
                VolumeType='gp3',
            )
            print(f"Volume {volume_id} modified to gp3.")
    except Exception as e:
       print(f"Failed to modify volume {volume_id}: {str(e)}")

    return {
        'statusCode': 200,
        'body': 'Volume modification check completed.'
