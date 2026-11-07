# Containerized Recipe Management System

A multi-tier microservices architecture demonstrating container orchestration, reverse proxy configuration, and backend API development.

## Architecture

This project consists of three main services orchestrated via Docker Compose:

- **Backend API (`app`)**: A Python REST API (Flask) for managing recipes.
- **Frontend Dashboard (`dashboard`)**: A web interface for interacting with the recipe data.
- **Reverse Proxy (`nginx`)**: An Nginx server routing incoming traffic to the appropriate backend or frontend containers.

## Technologies Used

- **Python 3** (Flask)
- **Docker & Docker Compose**
- **Nginx**

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/) and Docker Compose installed on your local machine.

### Installation & Execution

1. Clone the repository:
   bash
   git clone [https://github.com/yourusername/dockerized-recipe-app.git](https://github.com/yourusername/dockerized-recipe-app.git)
   cd dockerized-recipe-app
   



2. Create a `.env` file in the root directory (you can use the provided `.env.example` as a template).
3. Build and run the containers:

bash
docker-compose up -d --build


4. Access the application:

- Dashboard: `http://localhost`
- API Endpoints: `http://localhost/api/...`

## Project Structure

- `/app` - Python backend source code and Dockerfile.
- `/dashboard` - Frontend static files (HTML/CSS/JS).
- `/nginx` - Nginx configuration files.
- `docker-compose.yml` - Services orchestration.
