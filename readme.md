# Booksapp

## Introduction

Booksapp is a Flask-based web application for managing books. It allows users to add, retrieve, update, delete, and search for books by title or author. This project is designed to demonstrate a RESTful API implementation with Flask and SQLAlchemy. It's containerized with Docker Compose for easy deployment and development, and managed with Poetry for Python dependency management. Project was designed with mysql backend to run inside docker.

## Getting Started

### Prerequisites

- Docker and Docker Compose (for running with Docker)
- Python 3.11 or higher (for running without Docker)
- Poetry for Python package management

### Running with Docker Compose

#### Start the Application

Navigate to the project directory and start the application using Docker Compose:

```bash
docker-compose up --build
```

This command builds the Docker images if they don't exist and starts the containers defined in your docker-compose.yml file, including the Flask application and any other services like a MySQL database and phpMyAdmin for database management.

#### Configuration via .env File

For local development and testing, this project utilizes a .env file to manage environment-specific settings. The .env file should be placed at the root of the project directory and is not checked into version control to keep sensitive information like database credentials secure.

##### Creating a .env File

To set up your local development environment, create a .env file in the root of the project with the following content:

```text
# .env example
DATABASE_USERNAME=your_database_username
DATABASE_PASSWORD=your_database_password
DATABASE_HOST=db
DATABASE_NAME=your_database_name
MYSQL_ROOT_PASSWORD=your_database_root_password
```

Replace your_database_username, your_database_password, your_database_root_password and your_database_name with your actual database credentials and information.

**Important Note**
The .env file is intended for development and testing purposes only. For production environments, it's recommended to set environment variables directly in your hosting environment or through a secure configuration service.

#### Accessing the Application

Once the containers are up and running, you can access the Flask application at <http://localhost:5000> and phpMyAdmin at <http://localhost:8080> (or whichever ports you have configured).

### Setting Up and Running with Poetry

#### Installation

If you don't have Poetry installed, install it by following the instructions on the Poetry website.

#### Project Setup

Clone the repository and navigate into the project directory:

```bash
git clone https://yourprojecturl.git
cd yourprojectdirectory
```

Install the project dependencies using Poetry:

```bash
poetry install
```

#### Running the Application

Activate the Poetry shell:

```bash
poetry shell
```

Run the Flask application:

```bash
flask run
```

Or directly with Poetry:

```bash
poetry run flask run
```

### Running Tests

Run the tests:

```bash
poetry run pytest
```

## Contributing

Contributions are welcome! Please read our Contributing Guide for details on how to submit pull requests to the project.

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
