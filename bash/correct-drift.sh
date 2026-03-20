terraform state rm aws_db_instance.poc
awk '{sub(/engine_version      = "8.0"/, "engine_version      = \"8.4.7\""); print}' rds.tf > tmp && mv tmp rds.tf
terraform import aws_db_instance.poc "poc-drift-mysql"