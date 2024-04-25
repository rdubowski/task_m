# URL shortener - FastAPI, React

## Prerequisites
Before you start, make sure you have the following installed on your machine:
- Docker
- Docker Compose

## Setup
To set up the project, follow these steps:

1. Clone the repository:

2. Navigate to the project directory:

3. Build and start the containers using Docker Compose:
    ```shell
    docker-compose up -d --build
    ```

4. Once the containers are up and running, you can access the API at:
    ```
    http://localhost:8004/
    ```

    And the frontend at:
    ```
    http://localhost:3000/
    ```

## Running Tests
To run the tests, you need to:
    ```
    docker-compose exec web pytest
    ```
