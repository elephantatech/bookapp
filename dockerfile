# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy the pyproject.toml and optionally poetry.lock files
COPY pyproject.toml poetry.lock* /app/

# Configure Poetry: 
# - Do not create a virtual environment inside the Docker container
# - Install dependencies from pyproject.toml (and poetry.lock if present)
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Copy the rest of your application code
COPY . /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the Flask application
CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]
