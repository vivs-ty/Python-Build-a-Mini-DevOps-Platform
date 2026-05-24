# Task 182: Delete unused cloud resources to optimize cost.

import boto3
from botocore.exceptions import ClientError

def terminate_stopped_instances():
    try:
        ec2 = boto3.client('ec2')
        response = ec2.describe_instances()
        
        terminated_count = 0
        for reservation in response.get('Reservations', []):
            for instance in reservation.get('Instances', []):
                instance_id = instance['InstanceId']
                state = instance['State']['Name']
                
                # Terminate the instance if it is currently stopped
                if state == 'stopped':
                    print(f"Terminating stopped instance {instance_id}...")
                    ec2.terminate_instances(InstanceIds=[instance_id])
                    terminated_count += 1
                    
        print(f"Total stopped instances terminated: {terminated_count}")
        
    except ClientError as e:
        print(f"AWS Error: {e}")

if __name__ == "__main__":
    terminate_stopped_instances()
    
   