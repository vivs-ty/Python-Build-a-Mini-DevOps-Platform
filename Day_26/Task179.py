# Task 179: Start and stop compute instances programmatically.

import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances()
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        state = instance['State']['Name']
        print(f"Instance ID: {instance_id}, State: {state}")
        
        # Example: Start the instance if it's stopped, or stop it if it's running
        if state == 'stopped':
            print(f"Starting instance {instance_id}...")
            ec2.start_instances(InstanceIds=[instance_id])
        elif state == 'running':
            print(f"Stopping instance {instance_id}...")
            ec2.stop_instances(InstanceIds=[instance_id])
print(f"Total instances processed: {len([instance for reservation in response['Reservations'] for instance in reservation['Instances']])}")
