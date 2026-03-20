resource "aws_db_instance" "poc" {
  identifier          = "poc-drift-mysql"
  engine              = "mysql"
  engine_version      = "8.0"        
  instance_class      = "db.t3.micro"
  allocated_storage   = 20
  db_name             = "pocdb"
  username            = "admin"
  password            = var.db_password
  skip_final_snapshot = true
  apply_immediately   = true
}
