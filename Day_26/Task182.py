# Task 182: Delete unused cloud resources to optimize cost.
#
# Required dependencies: pip install boto3

import boto3
from botocore.exceptions import ClientError

def terminate_stopped_instances(region_name='us-east-1'):
    try:
        ec2 = boto3.client('ec2', region_name=region_name)
        response = ec2.describe_instances()
        
        terminated_count = 0
        for reservation in response.get('Reservations', []):
            for instance in reservation.get('Instances', []):
                instance_id = instance['InstanceId']
                state = instance['State']['Name']
                
                # Terminate the instance if it is currently stopped
                if state == 'stopped':
                    print(f"Terminating stopped instance {instance_id}...")
                    term_response = ec2.terminate_instances(InstanceIds=[instance_id])
                    if term_response['ResponseMetadata']['HTTPStatusCode'] == 200:
                        print(f"Successfully terminated instance {instance_id}")
                        terminated_count += 1
                    
        print(f"Total stopped instances terminated: {terminated_count}")
        
    except ClientError as e:
        print(f"AWS Error: {e}")

if __name__ == "__main__":
    terminate_stopped_instances()
    
    print(" \n Python 30 days Series - Day 26 : Task 182 \n")
    print(" \n Day 26: Cloud Automation \n")
    print(" \n Have a good one! " + "-"*40)
