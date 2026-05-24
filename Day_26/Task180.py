# Task 180: Monitor cloud resource usage and log it.

import boto3
import logging
from botocore.exceptions import ClientError

# Configure logging to write directly to a file
logging.basicConfig(
    filename='cloud_resource_usage.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(message)s'
)

def log_instance_states():
    try:
        ec2 = boto3.client('ec2')
        response = ec2.describe_instances()
        
        count = 0
        for reservation in response.get('Reservations', []):
            for instance in reservation.get('Instances', []):
                instance_id = instance['InstanceId']
                state = instance['State']['Name']
                
                logging.info(f"Instance ID: {instance_id}, State: {state}")
                count += 1
                
        print(f"Logged states for {count} instances to 'cloud_resource_usage.log'")
        
    except ClientError as e:
        print(f"AWS Error: {e}")

if __name__ == "__main__":
    log_instance_states()
    
    print("\nPython 30 days Series - Day 26 : Task 180")
    print("Day 26 : Cloud Automation")
    print("Have a good one!\n" + "-"*40)
