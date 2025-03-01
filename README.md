# Country Population Aggregation Service

This project is an asynchronous web service developed using FastAPI that stores country population data in a PostgreSQL database. The service scrapes population data from multiple sources (Wikipedia) and aggregates it by regions.

## Description

- The project provides an API that allows retrieving aggregated data by regions based on the population data of countries.
- Country population data is stored in a PostgreSQL database.
- The service supports changing the data source through environment variables.
- The service is containerized using Docker Compose for easy setup and deployment in a containerized environment.

## Technologies

- **FastAPI** — for creating the asynchronous API.
- **PostgreSQL** — for data storage.
- **Docker** — for containerization.
- **SQLAlchemy** — for interacting with the database.
- **Alembic** — for database migrations.

## Installation and Setup

### Clone the repository

```bash
git clone https://github.com/vladlevkovich/population-test-task.git
cd population-aggregator
```

Make sure you have Docker and Docker Compose installed. To start the service, run:

### Build docker container
```bash 
docker-compose up --build
```

### Run docker container
```bash 
  docker-compose up get_data
  docker-compose up print_data
```
