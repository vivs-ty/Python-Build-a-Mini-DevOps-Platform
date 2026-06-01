# Task 181: Provision a new instance from predefined configuration.
#
# Required dependencies: pip install boto3
#
# Note: The ImageId (AMI) must exist in the AWS region you are deploying to.
# Get available AMIs for your region with:
#   aws ec2 describe-images --owners amazon --query 'Images[?Name==`amzn2-ami-hvm-*-x86_64-gp2`].ImageId' --region <your_region>

import boto3
from botocore.exceptions import ClientError

def provision_ec2_instance(image_id=None, region_name='us-east-1'):
    try:
        ec2 = boto3.client('ec2', region_name=region_name)
        
        # If no image_id provided, use a default Ubuntu 22.04 LTS AMI
        # Note: This AMI ID may vary by region, so we provide a parameter to override
        if image_id is None:
            # Get the most recent Ubuntu 22.04 LTS image
            images_response = ec2.describe_images(
                Owners=['099720109477'],  # Canonical
                Filters=[
                    {'Name': 'name', 'Values': ['ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*']},
                    {'Name': 'state', 'Values': ['available']}
                ]
            )
            
            if not images_response['Images']:
                print(f"Error: No Ubuntu images found in region {region_name}")
                return
            
            image_id = sorted(images_response['Images'], key=lambda x: x['CreationDate'])[-1]['ImageId']
            print(f"Using AMI: {image_id}")
        
        instance_config = {
            'ImageId': image_id,
            'MinCount': 1,
            'MaxCount': 1,
            'InstanceType': 't2.micro'
        }
        
        print("Provisioning new instance...")
        response = ec2.run_instances(**instance_config)
        
        if response['Instances']:
            instance_id = response['Instances'][0]['InstanceId']
            print(f"Successfully provisioned new instance with ID: {instance_id}")
        else:
            print("Error: No instances returned in response")
        
    except ClientError as e:
        print(f"AWS Error: {e}")

if __name__ == "__main__":
    provision_ec2_instance()

    print(" \n Python 30 days Series - Day 26 : Task 181 \n")
    print(" \n Day 26: Cloud Automation \n")
    print(" \n Have a good one! " + "-"*40)

    
