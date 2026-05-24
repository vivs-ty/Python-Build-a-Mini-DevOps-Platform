# Task 180: Monitor cloud resource usage and log it.

import boto3
import logging

# Configure logging
logging.basicConfig(filename='cloud_resource_usage.log', level=logging.INFO, format='%(asctime)s - %(message)s')
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        state = instance['State']['Name']
        logging.info(f"Instance ID: {instance_id}, State: {state}")
print(f"Total instances monitored: {len([instance for reservation in response['Reservations'] for instance in reservation['Instances']])}")
