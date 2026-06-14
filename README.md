# 🎓 Internship & Job Tracking Dashboard

A containerized, multi-page web application built with Streamlit and PostgreSQL. This system is designed to help university faculty internally track, manage, and analyze student internship and job opportunities.

## 👥 Team Members
* **Rana M. Zain Zahid** (Member 1) - Infrastructure, Core Analytics, Alert Systems
* **Usman Butt** (Member 2) - CRUD Operations, Data Validation, CSV Integration
* **Abdullah** (Member 3) - Dashboards, Search Engines, Duplicate Detection

---

## 🏗️ System Architecture
The application runs entirely within a Docker Compose environment, orchestrating three main services:

* **Streamlit App Container:** The frontend user interface operating on port 8501.
* **PostgreSQL Container:** The persistent backend database operating on port 5433 (mapped to 5432 internally).
* **pgAdmin Container:** The graphical database management tool operating on port 5050.

---

## 🚀 Setup & Execution

### Prerequisites
* Docker Desktop installed and running.
* Git installed.

### Installation Steps
1. **Clone the repository:**
```bash
   git clone <your-repository-url>
   cd streamlit-postgres-assignment

```

2. **Start the environment:**

```bash
   docker compose up -d --build

```

3. **Access the Application:**
* **Streamlit Dashboard:** Navigate to `http://localhost:8501` in your browser.
* **pgAdmin Database Manager:** Navigate to `http://localhost:5050` (Login: `admin@example.com` / `admin123`).



---

## 🐳 Docker Compose Concepts Explained

Our `docker-compose.yml` file utilizes several core Docker concepts to manage the multi-container environment:

* **`services`:** Defines the individual containers (postgres_db, pgadmin, streamlit_app) that make up the application.
* **`image`:** Specifies pre-built base images from Docker Hub (e.g., `postgres:16`, `dpage/pgadmin4:latest`).
* **`build`:** Tells Docker to build a custom image using the provided `Dockerfile` in the current directory (`build: .`).
* **`ports`:** Maps internal container ports to external host machine ports (e.g., `"5050:80"`) so we can access them via `localhost`.
* **`environment`:** Passes environmental variables (like database passwords and usernames) into the containers at runtime.
* **`volumes`:** Maps container storage to persistent named volumes (e.g., `postgres_data`) so database records are not lost when the container stops.
* **`depends_on`:** Ensures services start in the correct order (Streamlit and pgAdmin wait for Postgres to initialize).
* **`restart`:** The `unless-stopped` policy ensures containers automatically restart if they crash or if the host machine reboots.
* **Service Name-Based Connection:** Inside the Docker network, containers communicate using their service names instead of IP addresses. Streamlit connects to the database using `host=postgres_db`.

---

## 💻 Docker Commands Guide

Here are the essential Docker commands used to manage this project:

* `docker compose up -d`: Starts all services in detached mode (in the background).
* `docker compose ps`: Checks the status of running services and their mapped ports.
* `docker compose logs postgres_db`: Views the logs specifically for the PostgreSQL container.
* `docker compose logs pgadmin`: Views the logs specifically for the pgAdmin container.
* `docker compose logs streamlit_app`: Views the logs specifically for the Streamlit app container.
* `docker compose down`: Stops and removes the containers and network while preserving the named volumes and database data.
* `docker volume ls`: Lists all Docker volumes currently stored on the host machine.
* `docker compose down -v`: A destructive command that stops containers and completely removes the mapped volumes, resulting in permanent database data deletion.

---

## 🛠️ GitHub Collaboration Workflow

Our group followed a strict version control policy to ensure equal contribution:

1. The repository was initialized with a `.gitignore` file to prevent pushing local `.env` files and `__pycache__`.
2. Every group member cloned the repository locally to their respective machines.
3. Members worked independently on assigned modules (M1: Infrastructure, M2: CRUD, M3: Analytics).
4. We used `git add .`, `git commit -m "descriptive message"`, and `git push` to integrate changes to the main branch.
5. Commit history reflects distributed, meaningful contributions across the project timeline from all three members.

---

## ⚠️ Common Errors & Troubleshooting

During development, we encountered and documented the following common errors:

1. **Port 5432 Already in Use:**
* *Error:* Docker failed to start with `Bind for 0.0.0.0:5432 failed`.
* *Solution:* A local Windows Postgres service was occupying the port. We resolved this by changing the host port mapping in `docker-compose.yml` to `"5433:5432"`.


2. **PostgreSQL Container Crashing Immediately:**
* *Error:* The `opportunity_postgres` container was stuck in a restart loop.
* *Solution:* Using the `postgres:latest` image pulled version 18, which conflicts with standard volume directory structures. We resolved this by pinning the image version to `postgres:16` and using `docker compose down -v` to clear the corrupted volume.


3. **Streamlit Cannot Connect to Database:**
* *Error:* `could not translate host name "postgres_db" to address`.
* *Solution:* The Docker internal network was corrupted due to earlier container crashes. We resolved this by running a clean `docker compose down` followed by `docker compose up -d --build` to re-establish the network bridge.


4. **pgAdmin Unable to Connect:**
* *Error:* Connection timeout when registering the server.
* *Solution:* We ensured the "Host name/address" in pgAdmin was set to the Docker service name (`postgres_db`) rather than `localhost` or an IP address.