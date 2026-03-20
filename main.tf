terraform {

  backend "s3" {}
}

provider "aws" {
  region = var.aws_region
}

variable "aws_region" {
  description = "AWS region for provider resources"
  type        = string
  default     = "us-east-1"
}