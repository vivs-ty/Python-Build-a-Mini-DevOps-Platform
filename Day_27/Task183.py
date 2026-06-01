# Task 183: Tag cloud resources and filter them by tags.
#
# Required dependencies: pip install boto3

import boto3
from botocore.exceptions import ClientError

def tag_and_filter_instances(instance_id, tag_key, tag_value, region_name='us-east-1'):
    if not instance_id or instance_id == "i-0123456789abcdef0":
        print("Error: Please provide a valid instance ID. Example: i-0123456789abcdef0")
        return
        
    try:
        ec2 = boto3.client('ec2', region_name=region_name)
        
        # Tag the resource
        print(f"Adding tag {tag_key}={tag_value} to instance {instance_id}...")
        tag_response = ec2.create_tags(
            Resources=[instance_id],
            Tags=[{'Key': tag_key, 'Value': tag_value}]
        )
        print("Tag added successfully.")
        
        # Filter resources by the newly added tag
        print(f"\nFiltering instances by tag {tag_key}={tag_value}...")
        response = ec2.describe_instances(
            Filters=[{'Name': f'tag:{tag_key}', 'Values': [tag_value]}]
        )
        
        found_count = 0
        for reservation in response.get('Reservations', []):
            for instance in reservation.get('Instances', []):
                print(f"Found Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}")
                found_count += 1
        
        if found_count == 0:
            print(f"No instances found with tag {tag_key}={tag_value}")
                
    except ClientError as e:
        print(f"AWS Error: {e}")

if __name__ == "__main__":
    # Replace with your actual instance ID
    # Example: tag_and_filter_instances("i-0123456789abcdef0", "Environment", "Production")
    print("Please provide a valid instance ID to tag and filter.")
    print("Example usage: tag_and_filter_instances('i-0123456789abcdef0', 'Environment', 'Production')")
    
    print(" \n Python 30 days Series - Day 27 : Task 183 \n")
    print(" \n Day 27: Cloud Tagging and CI/CD Basics \n")
    print(" \n Have a good one! " + "-"*40)
    