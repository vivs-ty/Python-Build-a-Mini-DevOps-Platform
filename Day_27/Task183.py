# Task 183: Tag cloud resources and filter them by tags.

import boto3
from botocore.exceptions import ClientError

def tag_and_filter_instances(instance_id, tag_key, tag_value):
    try:
        ec2 = boto3.client('ec2')
        
        # Tag the resource
        print(f"Adding tag {tag_key}={tag_value} to instance {instance_id}...")
        ec2.create_tags(
            Resources=[instance_id],
            Tags=[{'Key': tag_key, 'Value': tag_value}]
        )
        print("Tag added successfully.")
        
        # Filter resources by the newly added tag
        print(f"\nFiltering instances by tag {tag_key}={tag_value}...")
        response = ec2.describe_instances(
            Filters=[{'Name': f'tag:{tag_key}', 'Values': [tag_value]}]
        )
        
        for reservation in response.get('Reservations', []):
            for instance in reservation.get('Instances', []):
                print(f"Found Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}")
                
    except ClientError as e:
        print(f"AWS Error: {e}")

if __name__ == "__main__":
    # Replace with your actual instance ID
    tag_and_filter_instances("i-0123456789abcdef0", "Environment", "Production")
    
    print("\nPython 30 days Series - Day 27 : Task 183")
    print("Day 27 : Cloud Tagging and CI/CD Basics")
    print("Have a good one!\n" + "-"*40)
    