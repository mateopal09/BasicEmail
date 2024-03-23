module "ec2" {
  source       = "./modules/aws_ec2"
  project_name = var.project_name
  key_name     = var.key_name
}

module "mysql" {
  source       = "./modules/aws_rds_mysql"
  project_name = var.project_name
  username     = var.db_username
  password     = var.db_password
}
