# Task 179: Start and stop compute instances programmatically.

import boto3
from botocore.exceptions import ClientError

def toggle_ec2_instances():
    try:
        ec2 = boto3.client('ec2')
        response = ec2.describe_instances()
        
        processed_count = 0
        for reservation in response.get('Reservations', []):
            for instance in reservation.get('Instances', []):
                instance_id = instance['InstanceId']
                state = instance['State']['Name']
                
                # Start the instance if it's stopped, stop it if it's running
                if state == 'stopped':
                    print(f"Starting instance {instance_id}...")
                    ec2.start_instances(InstanceIds=[instance_id])
                    processed_count += 1
                elif state == 'running':
                    print(f"Stopping instance {instance_id}...")
                    ec2.stop_instances(InstanceIds=[instance_id])
                    processed_count += 1
                    
        print(f"Total instances processed: {processed_count}")
        
    except ClientError as e:
        print(f"AWS Error: {e}")

if __name__ == "__main__":
    toggle_ec2_instances()
    
 