# Task 182: Delete unused cloud resources to optimize cost.

import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        state = instance['State']['Name']
        print(f"Instance ID: {instance_id}, State: {state}")
        
        # Example: Terminate the instance if it's stopped
        if state == 'stopped':
            print(f"Terminating instance {instance_id}...")
            ec2.terminate_instances(InstanceIds=[instance_id])
print(f"Total instances processed for deletion: {len([instance for reservation in response['Reservations'] for instance in reservation['Instances'] if instance['State']['Name'] == 'stopped'])}")  
