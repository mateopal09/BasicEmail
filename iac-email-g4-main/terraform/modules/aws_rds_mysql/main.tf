# SECURITY GROUP FOR RDS MySQL DATABASE

resource "aws_security_group" "sg_mysql" {
  name = "sg_mysql"

  ingress {
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

}



# RDS MYSQL DATABASE

resource "aws_db_instance" "mysql" {
  engine            = "mysql"
  engine_version    = "8.0.35"
  instance_class    = "db.t3.micro"
  allocated_storage = 20
  storage_type      = "gp2"
  identifier        = "email-project-db-g4"
  db_name           = "email_project_g4"


  username = var.username
  password = var.password

  skip_final_snapshot          = true
  multi_az                     = false
  backup_retention_period      = 0
  delete_automated_backups     = true
  publicly_accessible          = true
  performance_insights_enabled = false

  vpc_security_group_ids = [aws_security_group.sg_mysql.id]

  tags = {
    project = var.project_name
  }


}
