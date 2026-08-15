# Flask DevOps Project

A simple Flask application created as a practical DevOps project.

The project demonstrates the basic application deployment workflow using **Python, Flask, Docker, Docker Compose, Ansible, and pytest**.

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

The Flask application provides two endpoints.

### `GET /`

Returns a simple response confirming that the application is running.

```text
Hello from Docker! Simple Flask app is working.
```

### `GET /health`

Health check endpoint.

```json
{
  "status": "ok"
}
```

The endpoint can be used by monitoring or orchestration systems to verify that the application is responding.

---

## Run Locally

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
python app/app.py
```

The application will listen on:

```text
http://localhost:5000
```

Test the endpoints:

```bash
curl http://localhost:5000
curl http://localhost:5000/health
```

---

## Run with Docker Compose

Build and start the application:

```bash
docker compose up --build
```

Docker Compose maps the container port `5000` to host port `5001`:

```text
Host:5001 → Container:5000
```

The application is available at:

```text
http://localhost:5001
```

Test the endpoints:

```bash
curl http://localhost:5001
curl http://localhost:5001/health
```

Stop the application:

```bash
docker compose down
```

---

## Testing

The project uses **pytest** for application testing.

Run tests from the project root:

```bash
pytest
```

The current test verifies the `/health` endpoint:

* HTTP status code is `200`
* response contains the expected JSON

Example:

```text
============================= test session starts =============================
collected 1 item

tests/test_app.py .                                                     [100%]

============================== 1 passed ======================================
```

---

## Ansible Deployment

The project contains an Ansible playbook for deploying the application to a Linux host.

The playbook performs the following tasks:

1. Updates the APT package cache
2. Installs Docker and Docker Compose
3. Starts and enables the Docker service
4. Creates the application directory
5. Creates the application files
6. Builds the Docker image
7. Starts the application with Docker Compose

Run the deployment:

```bash
cd ansible-flask-deploy
ansible-playbook -i inventory.ini playbook.yml
```

The deployed application is available on the configured host port:

```text
http://localhost:5001
```

---

## Deployment Flow

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
    ├── Configure application
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

## DevOps Concepts Demonstrated

This project is focused on practicing the following DevOps fundamentals:

* Linux administration
* Docker containerization
* Docker Compose
* Infrastructure automation with Ansible
* Application health checks
* Automated application testing
* Basic deployment automation
* Git-based development workflow

## Current Scope

The project intentionally remains small so that each component can be understood and maintained easily.

Planned improvements may include:

* CI/CD pipeline
* Docker image registry
* PostgreSQL
* Nginx reverse proxy
* Gunicorn
* Prometheus and Grafana
* Additional automated tests
* Secrets management

## Author

**Alexandr Prohnitskii**

DevOps Engineer

