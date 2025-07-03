# Lendesk Platform Challenge

GitHub Actions + Docker coding challenge for Platform developers.

Welcome! This challenge will test your ability to work with Docker and GitHub Actions in a realistic CI scenario. Your task is to take a small web API and containerize it, then write a CI workflow that builds and tests the app inside GitHub Actions.

This challenge is expected to take about 1 hour.

## Objectives

- Containerize the app and the database using Docker
- Create a GitHub Actions workflow that:
  - Builds the Docker image
  - Starts the application and database
  - Runs automated tests against the running container

## Requirements

### Docker

- Create a `Dockerfile` to containerize the app
- Create a `docker-compose.yml` to orchestrate the build
  - Should include two services: the app and the database

### GitHub Actions

Develop and test this in your own private GitHub repository. You do not need to share this repository with us.

_GitHub Free accounts get [2,000 free GitHub Actions minutes](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions) per month for private repositories._

- Create a `build.yml` GitHub Action workflow
  - Build the app image "locally" within GitHub Actions (do not push to Docker Hub)
  - Start the containers using Docker Compose
  - Test the app by making curl commands to the `/ping` and `/users` endpoints
    - The workflow should fail if one of these requests is unsuccessful
  - Tear down the environment

### Artifacts

Return to us the following items:

- A ZIP file containing the code for this challenge
- Screenshot(s) of successful GitHub Actions run
