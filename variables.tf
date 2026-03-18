# variables.tf
variable "db_password" {
  type      = string
  sensitive = true
  default   = "pocpassword123"
}
