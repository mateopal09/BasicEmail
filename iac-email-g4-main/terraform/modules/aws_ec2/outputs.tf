output "public_ip" {
  value       = aws_instance.ec2.public_ip
  description = "The public IP of the EC2 instance"
}
