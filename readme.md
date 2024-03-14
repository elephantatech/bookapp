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

If you don't have Poetry installed, install it by following the instructions on the [Poetry website](https://python-poetry.org/).

#### Project Setup

Clone the repository and navigate into the project directory:

```bash
git clone git@github.com:elephantatech/bookapp.git
cd bookapp
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

We welcome contributions from the community and are pleased to have you join us. Here are some guidelines that will help you get started:

1. Code of Conduct: By participating in this project, you agree to abide by its Code of Conduct.

2. Getting Started: Take a look at the open issues for areas where you can contribute. Issues labeled good first issue are a great place to start.

3. Fork and Clone: Fork the project to your GitHub account and clone your fork to your local machine.

4. Environment Setup: Follow the setup instructions in the project README to get your development environment ready.

5. Branching Strategy: Create a new branch for each feature, improvement, or bug fix. Use a descriptive name for your branch, such as feature/add-search-functionality or fix/login-issue.

6. Make Changes: Implement your changes, adhering to the coding standards and guidelines mentioned in the project documentation.

7. Write Tests: Ensure that your changes are accompanied by tests, if applicable. Run the existing test suite to ensure that your changes do not break existing functionality.

8. Commit Messages: Write clear and meaningful commit messages. Include a brief description of the changes and reference related issue numbers if any.

9. Submit a Pull Request (PR): Push your changes to your fork and submit a pull request to the main project. Provide a detailed description of the changes and reference the related issue(s).

10. PR Review: Wait for the PR review. Be open to feedback and make necessary adjustments. Your PR may require several rounds of review and updates before merging.

**NOTE: You can always open an issue to ask questions or reach out on x at [@elephantatech](https://twitter.com/elephantatech)**

## License

Copyright 2024 elephanta technologies and design inc (elephantatech)

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

   [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
