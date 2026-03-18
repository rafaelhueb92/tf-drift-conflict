import boto3
import time

REGION = "us-east-1"
DB_IDENTIFIER = "poc-drift-mysql"

rds = boto3.client("rds", region_name=REGION)

while True:
    resp = rds.describe_db_instances(DBInstanceIdentifier=DB_IDENTIFIER)
    status = resp["DBInstances"][0]["DBInstanceStatus"]
    version = resp["DBInstances"][0]["EngineVersion"]
    if status == "available":
        print("Upgrade complete!")
        break
    print(f"Status: {status} | Version: {version}")
    time.sleep(30)
