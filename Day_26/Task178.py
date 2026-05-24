# Task 178: List all instances or resources in a cloud environment.

import boto3
from botocore.exceptions import ClientError

def list_ec2_instances():
    try:
        ec2 = boto3.client('ec2')
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
    
    print("\nPython 30 days Series - Day 26 : Task 178")
    print("Day 26 : Cloud Automation")
    print("Have a good one!\n" + "-"*40)
    