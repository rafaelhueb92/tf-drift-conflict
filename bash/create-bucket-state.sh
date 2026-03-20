ACCOUNT=$(aws sts get-caller-identity --query Account --output text)
aws s3api create-bucket --bucket tfstate-$ACCOUNT