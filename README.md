# UPDATES EMAIL HOME GROUP 4

This document provides an overview of the updates to the Home Group 4 project made by Home Group 3. See [Frontend](https://github.com/G3-VER-TECH-FELLOWS/email-G4/blob/main/front-email-g4-main/README.md), [Backend](https://github.com/G3-VER-TECH-FELLOWS/email-G4/blob/main/back-email-g4-main/README.md) and [IAC](https://github.com/G3-VER-TECH-FELLOWS/email-G4/blob/main/iac-email-g4-main/README.md) for more detailed updates and implementations.

## Frontend Changes Overview

- Removed `.dockerignore` file, which included various Python, Git, and environment-specific files to ignore during Docker builds.
- Added a new ESLint configuration file `.eslintrc.cjs` focusing on TypeScript and React rules.
- Introduced Continuous Deployment (CD) and Continuous Integration (CI) pipelines with GitHub Actions, specified in `.github/workflows/cd.yml` and `.github/workflows/ci.yml`.
- Updated the Docker configuration, introducing a multi-stage build in `Dockerfile` for optimizing the build process.
- Added a `docker-compose.yml` file for defining and running multi-container Docker applications, setting up the project with specific ports and environment variables.
- Configured Nginx for serving the application through a new `default.conf` file.
- Updated `index.html` to serve as the entry point for the web application, including references to the main JavaScript file and the project's title.
- Significant updates to `package.json`, including changes to project name, version, scripts, dependencies, and development dependencies.
- Introduced `postcss.config.js` for PostCSS configuration, enabling plugins like Tailwind CSS and Autoprefixer.
- Refactored code across various components (`ComposeView.tsx`, `InboxView.tsx`, `Message.tsx`, etc.) for improvements and removal of unused imports.
- Adjustments in context files (`SelectedEmailContext.tsx`, `UserContext.tsx`, etc.) and icon components to clean up imports and code structure.
- API configuration changes in `src/api.ts` to point to new backend endpoints.
- File structure changes, including the renaming of `src/index.tsx` to `src/main.tsx` and addition of `src/vite-env.d.ts` for Vite-specific types.
- Created a startup script `start.sh` for setting up environment variables and starting Nginx in Docker containers.
- Updated Tailwind CSS configuration in `tailwind.config.js` for simplifying the setup.
- Overhauled TypeScript configuration in `tsconfig.json` and added `tsconfig.node.json` for specific settings related to Node.js environments.
- Introduced a Vite configuration file `vite.config.ts` for customizing the build process and integrating React with SWC.

## Backend Changes Overview

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

## IAC Implementation Overview

Infrastructure as Code (IAC) implementation with Terraform and Ansible offers numerous benefits for businesses, including streamlined deployment, enhanced performance, and cost savings. By automating infrastructure provisioning and management, organizations can achieve greater efficiency, scalability, and agility in their operations. Regular monitoring and optimization are essential for maximizing the effectiveness of the implemented solution and ensuring ongoing success.

## C4 Diagram
### Container diagram

![Container_diagram](./md-assets/diagram_g4_container.jpg)

### Component diagram

![Container_diagram](./md-assets/diagram_g4_component.jpg)

## Summary

- Frontend: The project has undergone significant updates, including the removal of certain files, introduction of new configurations for ESLint, Docker, Nginx, GitHub Actions CI/CD pipelines, and updates to package dependencies and scripts. Code refactoring was performed across various components and contexts to improve maintainability and performance. Additionally, the build and deployment processes have been optimized with the introduction of Vite and updated Docker configurations.
- Backend: Relevant changes were made to some modules, finding a way to solve some important technical issues, as well as efforts to standardize some files and modules so that they could be read more easily.
- IAC: As businesses grow and evolve, the demand for scalable, reliable, and efficient infrastructure becomes increasingly crucial. Manual infrastructure provisioning and configuration are prone to errors, inconsistencies, and inefficiencies. Therefore, automating these processes using IAC tools like Terraform and Ansible can significantly improve operational efficiency, reduce downtime, and enhance agility.
