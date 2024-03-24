# BACK EMAIL HOME GROUP 4

This is the backend that handles the logic for an email client. The modules are distributed in a layered architecture (models, service, controller)

This document provides an overview of the recent updates to the project, detailing the significant changes in the configuration, codebase, and infrastructure.

| Files and Folders          | Details                           |
| -------------------------- | --------------------------------- |
| [models](./models.py)      | Contains all models               |
| [services](./services)     | Contain service send_email and login |
| [controller](./controller) | Contain 5 controllers             |

## Changes Overview

- Code is modified `MyUserManager` class to encrypt the password.
- The views are separated into a module with independent files as controllers.
- The code that calls the actions in the database in the login and send_email.
- Controller are organized into service modules.
- The `service_send_email` code is simplified by validating the code with try and except
- APIs are documented using swagger, modifying the project setting.
- Changing the connection from postgres to mysql to a rds instance in AWS.
- `Docker compose` is updated and the creation of the db is skipped
- .env folder is created to hold sensitive keys
- `python `decouple` is installed to manage the enviroments variables
- `.dockerignore` is update with .env file
- `Setting` update to add the new DNS and connections to the database located in AWS

## Summary

Relevant changes were made to some modules, finding a way to solve some important technical issues, as well as efforts to standardize some files and modules so that they could be read more easily.

## Tools

- Django
- Django Rest Framework
- Docker Compose
