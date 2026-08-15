# Flask DevOps Project

A small Flask application created as a practical DevOps project.

The project demonstrates a basic software delivery workflow using **Python, Flask, pytest, Docker, Docker Compose, Ansible, Git, and GitHub Actions**.

The main goal of the project is to practice application containerization, automated testing, infrastructure automation, and CI/CD fundamentals.

---

## Tech Stack

- Python 3.12
- Flask
- pytest
- Docker
- Docker Compose
- Ansible
- Git
- GitHub Actions
- Linux

---

## Project Structure

    flask_project/
    ├── app/
    │   ├── __init__.py
    │   └── app.py
    ├── tests/
    │   └── test_app.py
    ├── ansible-flask-deploy/
    │   ├── inventory.ini
    │   ├── playbook.yml
    │   └── README.md
    ├── .github/
    │   └── workflows/
    │       └── ci.yml
    ├── Dockerfile
    ├── docker-compose.yaml
    ├── requirements.txt
    ├── requirements-dev.txt
    └── README.md

---

## Application

The Flask application exposes several HTTP endpoints.

### GET /

Returns a simple message confirming that the application is running.

    Hello from Docker! Simple Flask app is working.

### GET /health

Health check endpoint.

    {
      "status": "ok"
    }

This endpoint can be used by monitoring systems, load balancers, or container orchestration platforms to verify that the application is responding.

### GET /info

Returns basic application information.

    {
      "app": "flask_project",
      "version": "1.0"
    }

### GET /version

Returns the current application version.

    {
      "version": "1.0"
    }

---

## Run Locally

Create a virtual environment:

    python3 -m venv .venv

Activate it:

    source .venv/bin/activate

Install application dependencies:

    pip install -r requirements.txt

Install development and testing dependencies:

    pip install -r requirements-dev.txt

Start the application:

    python app/app.py

The application listens on:

    http://localhost:5000

Test the endpoints:

    curl http://localhost:5000
    curl http://localhost:5000/health
    curl http://localhost:5000/info
    curl http://localhost:5000/version

---

## Testing

The project uses **pytest** for automated application testing.

Tests are stored in:

    tests/test_app.py

Run tests from the project root:

    pytest

The tests currently verify:

- `/health` returns HTTP `200`
- `/health` returns the expected JSON response
- `/info` returns the expected application information
- `/version` returns the expected version

Example:

    ============================= test session starts =============================
    collected 3 items

    tests/test_app.py ...                                                     [100%]

    ============================== 3 passed =======================================

---

## Docker

The application can be built and run as a Docker container.

Build the image:

    docker build -t flask-app .

Run the container:

    docker run -d -p 5001:5000 flask-app

The port mapping is:

    Host :5001 → Container :5000

The Flask application listens on port `5000` inside the container.

The application is therefore available from the host at:

    http://localhost:5001

---

## Docker Compose

The project also includes a Docker Compose configuration.

Build and start the application:

    docker compose up --build

The Compose configuration maps:

    Host :5001 → Container :5000

Test the application:

    curl http://localhost:5001
    curl http://localhost:5001/health
    curl http://localhost:5001/info
    curl http://localhost:5001/version

Stop the application:

    docker compose down

---

## Ansible Deployment

The project includes an Ansible playbook for automated deployment to a Linux host.

The playbook is responsible for:

1. Updating the APT package cache
2. Installing Docker and Docker Compose
3. Starting and enabling the Docker service
4. Creating the application directory
5. Deploying the application
6. Starting the application using Docker Compose

Run the deployment:

    cd ansible-flask-deploy
    ansible-playbook -i inventory.ini playbook.yml

The application is then available on the configured host port:

    http://localhost:5001

---

## CI Pipeline

The project uses **GitHub Actions** for Continuous Integration.

The CI pipeline is triggered on:

- Pushes to the `develop` branch
- Pull requests targeting the `develop` branch

The current pipeline performs the following steps:

    Git Push / Pull Request
            │
            ▼
       GitHub Actions
            │
            ▼
       Setup Python
            │
            ▼
    Install dependencies
            │
            ▼
         Run pytest
            │
            ▼
     Build Docker image

If automated tests fail, the pipeline stops and the change is not considered valid.

---

## Development Workflow

The project follows a simple Git-based workflow:

    Developer
        │
        ▼
    Feature / change
        │
        ▼
      Git commit
        │
        ▼
    Push to develop
        │
        ▼
    GitHub Actions
        │
        ├── Run tests
        │
        └── Build Docker image

The `develop` branch is used for development and CI validation.

---

## Deployment Architecture

The current deployment architecture is intentionally simple:

    GitHub
       │
       │ push
       ▼
    GitHub Actions
       │
       ├──────────────┐
       │              │
       ▼              ▼
     pytest       Docker build
       │              │
       └───────┬──────┘
               │
               ▼
          Linux Host
               │
               ▼
         Docker Compose
               │
               ▼
        Flask Container
               │
          Container :5000
               │
               ▼
            Host :5001

The application itself listens on port `5000` inside the container.

Docker publishes this port on the host as `5001`:

    localhost:5001
           │
           ▼
         Docker
           │
           ▼
    Flask container:5000

---

## DevOps Concepts Demonstrated

This project is used to practice:

- Linux administration
- Git and Git branching
- Python application structure
- Automated testing with pytest
- Docker containerization
- Docker Compose
- Port mapping
- Infrastructure automation with Ansible
- Application health checks
- Continuous Integration
- GitHub Actions
- Basic CI/CD concepts

---

## Current Status

The project currently includes:

- Flask application
- Multiple HTTP endpoints
- Automated tests
- Dockerfile
- Docker Compose
- Ansible deployment
- GitHub Actions CI
- Docker image build in CI

### Planned Improvements

Possible future improvements include:

- Continuous Deployment
- Docker image registry
- Production WSGI server with Gunicorn
- Nginx reverse proxy
- PostgreSQL
- Prometheus and Grafana
- Additional automated tests
- Docker image versioning
- Secrets management
- Kubernetes deployment

---

## Author

**Alexandr Prohnitskii**

DevOps Engineer

