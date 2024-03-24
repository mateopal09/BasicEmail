output "db_instance_endpoint" {
  description = "The connection endpoint for the database instance."
  value       = aws_db_instance.mysql.endpoint
}

output "db_instance_address" {
  description = "The hostname of the database instance."
  value       = aws_db_instance.mysql.address
}

