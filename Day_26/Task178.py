# Task 178: List all instances or resources in a cloud environment.
#
# Required dependencies: pip install boto3

import boto3
from botocore.exceptions import ClientError

def list_ec2_instances(region_name='us-east-1'):
    try:
        ec2 = boto3.client('ec2', region_name=region_name)
        response = ec2.describe_instances()
        
        count = 0
        for reservation in response.get('Reservations', []):
            for instance in reservation.get('Instances', []):
                instance_id = instance['InstanceId']
                state = instance['State']['Name']
                print(f"Instance ID: {instance_id}, State: {state}")
                count += 1
                
        print(f"Total instances found: {count}")
        
    except ClientError as e:
        print(f"AWS Error: {e}")

if __name__ == "__main__":
    list_ec2_instances()
    
    print(" \n Python 30 days Series - Day 26 : Task 178 \n")
    print(" \n Day 26: Cloud Automation \n")
    print(" \n Have a good one! " + "-"*40)
    