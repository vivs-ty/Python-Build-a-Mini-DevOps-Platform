# Task 180: Monitor cloud resource usage and log it.
#
# Required dependencies: pip install boto3

import boto3
import logging
import os
from botocore.exceptions import ClientError

def log_instance_states(log_file='cloud_resource_usage.log', region_name='us-east-1'):
    # Configure logging to write directly to a file
    logging.basicConfig(
        filename=log_file, 
        level=logging.INFO, 
        format='%(asctime)s - %(message)s'
    )
    
    try:
        ec2 = boto3.client('ec2', region_name=region_name)
        response = ec2.describe_instances()
        
        count = 0
        for reservation in response.get('Reservations', []):
            for instance in reservation.get('Instances', []):
                instance_id = instance['InstanceId']
                state = instance['State']['Name']
                
                logging.info(f"Instance ID: {instance_id}, State: {state}")
                count += 1
                
        print(f"Logged states for {count} instances to '{log_file}'")
        
    except ClientError as e:
        print(f"AWS Error: {e}")

if __name__ == "__main__":
    log_instance_states()
    
    print(" \n Python 30 days Series - Day 26 : Task 180 \n")
    print(" \n Day 26: Cloud Automation \n")
    print(" \n Have a good one! " + "-"*40)
