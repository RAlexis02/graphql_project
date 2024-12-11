# graphql_project

# 🚀 GraphQL API Project


This project is a simple GraphQL API built with Python (Flask + Graphene). The API is containerized using Docker, making it easy to deploy and run anywhere. The purpose of this project is to provide an example of how to build and run a basic GraphQL API.

---

## 🌟 Features

- ⚡ **GraphQL API**: Query and fetch structured data easily.
- 🐳 **Dockerized**: Easy deployment using Docker.
- 📂 **Lightweight**: Simple project structure for quick setup.

---

## 🛠️ Requirements

To run this project, you'll need:

1. **Docker Installed**:
   - Download Docker from the official website: [Docker Desktop](https://www.docker.com/products/docker-desktop)
   - Ensure Docker is running before executing any commands.

2. **Verify Docker Installation**:
   Open a terminal or command prompt and run:

   ```bash
   docker --version
If installed correctly, you'll see the Docker version.

🚀 How to Run
Option 1: Pull and Run the Docker Image
Pull the Image: Open a terminal and run:

bash
Copiar código
docker pull rommela462/container.2
Run the Container:

bash
Copiar código
docker run -d -p 5000:5000 rommela462/container.2
Explanation:

-d: Runs the container in detached mode (background).
-p 5000:5000: Maps port 5000 on your machine to port 5000 in the container.
Access the API: Open your browser or API client (e.g., Postman) and go to: http://localhost:5000/graphql

Verify the Container: Check if the container is running:

bash
Copiar código
docker ps
This will list all active containers. Look for rommela462/container.2.

Stop the Container (optional):

bash
Copiar código
docker stop <container_id>
Remove the Container (optional):

bash
Copiar código
docker rm <container_id>
Option 2: Build and Run Locally
Clone the Repository:

bash
Copiar código
git clone https://github.com/RAlexis02/graphql_project.git
Navigate to the Project Directory:

bash
Copiar código
cd graphql_project
Build the Docker Image:

bash
Copiar código
docker build -t rommela462/container.2 .
Run the Container:

bash
Copiar código
docker run -d -p 5000:5000 rommela462/container.2
Access the API: Go to http://localhost:5000/graphql

Option 3: Using Docker Compose
Ensure Docker Compose File Exists: The docker-compose.yml file should look like this:

yaml
Copiar código
version: '3.8'
services:
  app:
    build: .
    ports:
      - "5000:5000"
Run Docker Compose:

bash
Copiar código
docker-compose up --build
Stop the Application:

bash
Copiar código
docker-compose down
🗂️ Project Structure
graphql
Copiar código
graphql_project/
├── app.py                # Main GraphQL API logic
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose configuration
└── requirements.txt      # Python dependencies
🌐 Testing the API
Open your browser and navigate to: http://localhost:5000/graphql

Run a sample GraphQL query:

graphql
Copiar código
query {
  hello
}
Verify the result:

json
Copiar código
{
  "data": {
    "hello": "Hello, GraphQL API!"
  }
}
🛠️ Troubleshooting
Docker Not Running: Ensure Docker Desktop is open and running.

Port Conflict: If port 5000 is in use, change the port mapping:

bash
Copiar código
docker run -d -p 8080:5000 rommela462/container.2
Then access the API at http://localhost:8080/graphql.

Permission Issues: Run commands with sudo on Linux if necessary:

bash
Copiar código
sudo docker run ...
📄 License
This project is open-source and available under the MIT License.