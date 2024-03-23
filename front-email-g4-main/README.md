# FRONT EMAIL HOME GROUP 4

This document provides an overview of the recent updates to the project, detailing the significant changes in the configuration, codebase, and infrastructure.

## Changes Overview

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

## Summary

The project has undergone significant updates, including the removal of certain files, introduction of new configurations for ESLint, Docker, Nginx, GitHub Actions CI/CD pipelines, and updates to package dependencies and scripts. Code refactoring was performed across various components and contexts to improve maintainability and performance. Additionally, the build and deployment processes have been optimized with the introduction of Vite and updated Docker configurations.

Please review the changes carefully and update your local development environments accordingly to ensure compatibility and take advantage of the new features and improvements.

---

## Optimization Docker Image

In the recent overhaul of our project's build and deployment process, significant changes were made to both the Vite configuration and the Nginx setup with the primary aim of drastically reducing the Docker image size. Previously, our Docker images were quite bulky, weighing in at around 1GB. This size not only impacted the efficiency of our deployment pipeline but also increased the resources required for running our application. By optimizing our Vite build process and streamlining our Nginx configuration, we managed to significantly pare down the Docker image size to a mere 21MB.

![docker](docs/image.png)