variable "access_key" {
  description = "The AWS access key"
  type        = string
}

variable "secret_key" {
  description = "The AWS secret key"
  type        = string
}

variable "region" {
  description = "The AWS region"
  type        = string
}

variable "project_name" {
  description = "The name of the project"
  type        = string
}

variable "key_name" {
  description = "The name of the key pair"
  type        = string
}

variable "db_username" {
  description = "The username for the database"
  type        = string
}

variable "db_password" {
  description = "The password for the database"
  type        = string
  
}
