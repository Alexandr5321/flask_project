# Flask DevOps Project

A simple Flask application used as a practical DevOps project.

The project demonstrates containerization, automated deployment with Ansible, Docker Compose, and basic application testing with pytest.

## Tech Stack

* Python
* Flask
* pytest
* Docker
* Docker Compose
* Ansible
* Linux

## Project Structure

```text
flask_project/
├── app/
│   ├── __init__.py
│   └── app.py
├── tests/
│   └── test_app.py
├── ansible-flask-deploy/
│   ├── inventory.ini
│   └── playbook.yml
├── Dockerfile
├── docker-compose.yaml
├── requirements.txt
├── pytest.ini
└── README.md
```

## Application

The application provides two endpoints.

### Home

```http
GET /
```

Response:

```text
Hello from Docker! Simple Flask app is working.
```

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

The `/health` endpoint can be used by monitoring systems or container orchestration platforms to check whether the application is responding.

## Run Locally

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app/app.py
```

The application will be available at:

```text
http://localhost:5000
```

Test the endpoints:

```bash
curl http://localhost:5000
curl http://localhost:5000/health
```

## Run with Docker Compose

Build and start the application:

```bash
docker compose up --build
```

The application will be available at:

```text
http://localhost:5001
```

Check the application:

```bash
curl http://localhost:5001
curl http://localhost:5001/health
```

Stop the application:

```bash
docker compose down
```

## Testing

The project uses pytest for basic application testing.

Run tests from the project root:

```bash
pytest
```

Example result:

```text
collected 1 item

tests/test_app.py .    [100%]

1 passed
```

The current test verifies that the `/health` endpoint:

* returns HTTP 200
* returns the expected JSON response

## Ansible Deployment

The project includes an Ansible playbook for deploying the application to a Linux server.

The playbook:

1. Updates the APT package cache
2. Installs Docker and Docker Compose
3. Starts and enables the Docker service
4. Creates the application directory
5. Deploys the application files
6. Builds and starts the Docker Compose application

Run the deployment:

```bash
cd ansible-flask-deploy
ansible-playbook -i inventory.ini playbook.yml
```

## Deployment Architecture

```text
Developer
    │
    ▼
   Git
    │
    ▼
Ansible
    │
    ├── Install Docker
    ├── Deploy application
    └── Start Docker Compose
                │
                ▼
        ┌───────────────┐
        │    Docker     │
        │               │
        │    Flask      │
        │   Container   │
        └───────┬───────┘
                │
             :5000
                │
                ▼
          Host :5001
```

## Goals

This project is primarily focused on practicing DevOps fundamentals:

* Linux administration
* Docker containerization
* Docker Compose
* Infrastructure automation with Ansible
* Application health checks
* Automated testing
* Basic deployment workflow

## Future Improvements

Possible future improvements include:

* CI/CD pipeline
* Docker image registry
* PostgreSQL database
* Nginx reverse proxy
* Prometheus and Grafana monitoring
* Improved test coverage
* Production-ready Gunicorn configuration
* Secrets management

---

## Author

**Alexandr Prohnitskii**

DevOps Engineer
