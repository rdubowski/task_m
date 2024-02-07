# task_m

## Prerequisites
Before start you need docker and docker-compose

## Setup:

Start with docker-compose 
`docker-compose up -d --build`

Api exposed on: `http://localhost:8004/`
Frontend exposed on: `http://localhost:3000/`

## Runing tests:
`docker-compose exec web pytest`