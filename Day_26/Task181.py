# Task 181: Provision a new instance from predefined configuration.

import boto3
from botocore.exceptions import ClientError

def provision_ec2_instance():
    try:
        ec2 = boto3.client('ec2')
        
        # Note: The ImageId (AMI) must exist in the AWS region you are deploying to
        instance_config = {
            'ImageId': 'ami-0c08d41d8a5d4b1f9',
            'MinCount': 1,
            'MaxCount': 1,
            'InstanceType': 't2.micro'
        }
        
        print("Provisioning new instance...")
        response = ec2.run_instances(**instance_config)
        
        instance_id = response['Instances'][0]['InstanceId']
        print(f"Successfully provisioned new instance with ID: {instance_id}")
        
    except ClientError as e:
        print(f"AWS Error: {e}")

if __name__ == "__main__":
    provision_ec2_instance()
    
