import boto3
import time

REGION = "us-east-1"
DB_IDENTIFIER = "poc-drift-mysql"

rds = boto3.client("rds", region_name=REGION)

print("Upgrading engine version to MySQL 8.4...")
rds.modify_db_instance(
    DBInstanceIdentifier=DB_IDENTIFIER,
    EngineVersion="8.4",
    AllowMajorVersionUpgrade=True,
    ApplyImmediately=True
)

while True:
    resp = rds.describe_db_instances(DBInstanceIdentifier=DB_IDENTIFIER)
    status = resp["DBInstances"][0]["DBInstanceStatus"]
    version = resp["DBInstances"][0]["EngineVersion"]
    print(f"Status: {status} | Version: {version}")
    if status == "available":
        print("Upgrade complete!")
        break
    time.sleep(30)
