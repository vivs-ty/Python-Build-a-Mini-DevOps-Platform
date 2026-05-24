# Task 178: List all instances or resources in a cloud environment.

import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances()
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}")

print(f"Total instances found: {len([instance for reservation in response['Reservations'] for instance in reservation['Instances']])}")
