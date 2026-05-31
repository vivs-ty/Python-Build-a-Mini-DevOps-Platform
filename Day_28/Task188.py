# Task 188: Roll back a deployment automatically when a pipeline fails.


def deploy_application(version):
    print(f"Attempting to deploy version: {version}...")
    # Simulating a deployment error
    raise Exception("Database migration failed during deployment.")

def rollback_application(previous_version):
    print(f"Initiating rollback to stable version: {previous_version}...")
    print("Rollback completed successfully. System is stable.")

def run_deployment_pipeline():
    current_version = "v2.0"
    stable_version = "v1.9"
    
    try:
        deploy_application(current_version)
        print("Deployment successful!")
    except Exception as e:
        print(f"Pipeline Failed: {e}")
        rollback_application(stable_version)

if __name__ == "__main__":
    run_deployment_pipeline()
    
    print("\nPython 30 days Series - Day 28 : Task 188")
    print("Day 28 : CI/CD Automation")
    print("Have a good one!\n" + "-"*40)
    
