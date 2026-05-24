# Task 181: Provision a new instance from predefined configuration.

import boto3
ec2 = boto3.client('ec2')
# Example configuration for a new instance
instance_config = {
    'ImageId': 'ami-0c08d41d8a5d4b1f9',
    'MinCount': 1,
    'MaxCount': 1,
    'InstanceType': 't2.micro'
}
response = ec2.run_instances(**instance_config)
instance_id = response['Instances'][0]['InstanceId']
print(f"Provisioned new instance with ID: {instance_id}")
