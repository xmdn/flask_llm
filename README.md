# Flask LLM Chat Application

This is a chat application built with a Flask backend and React frontend, using Clean Architecture principles. The backend integrates with OpenAI's API to provide conversational responses, and the light weight CDN based frontend offers a user-friendly chat interface with a sidebar for chat history. The application is containerized using Docker.

## Features
- **Backend**: Flask with Gunicorn, using OpenAI's API for chat responses.
- **Frontend**: React with Tailwind CSS, featuring a chat interface and history sidebar.
- **Architecture**: Clean Architecture with separated controllers, services, and models.
- **Deployment**: Dockerized with `docker-compose` for easy setup.
- **Configuration**: Environment variables via `.env` for GPT API key.

## Prerequisites
- **Windows**: Windows 10/11 with PowerShell.
- **WSL 2.0**: Ubuntu-20.04 installed in WSL.
- **Docker Desktop**: Configured for WSL 2.0 integration.
- **Git**: For cloning and managing the repository.
- **Python**: Version 3.11 (handled by Docker).
- **Node.js**: Not required (React uses CDN).
- **OpenAI API Key**: Obtain from [OpenAI Dashboard](https://platform.openai.com/).

## Setup Instructions

### 1. Clone the Repository
```powershell
cd D:\flask_llm
git clone https://github.com/xmdn/flask_llm.git .
```

### 2. Configure Environment Variables
Change `.env_example` to `.env` file in `D:\flask_llm` with the following:
```env
OPENAI_API_KEY=sk-proj-your-api-key-here
```
- Replace `sk-proj-your-api-key-here` with your OpenAI API key.
- Ensure `.env` is listed in `.gitignore` to prevent committing sensitive data.

### 3. Build and Run with Docker
```powershell
cd D:\flask_llm
wsl docker-compose build
wsl docker-compose up -d
```
- This starts the Flask backend on `http://localhost:8045` and the React frontend on `http://localhost:8080`.

### 4. Verify Services
- Check containers:
  ```powershell
  docker ps
  ```
- View Flask logs:
  ```powershell
  docker logs <flask_container_name>
  ```
- Test the backend:
  ```powershell
  curl -X POST http://localhost:8055/chat -H "Content-Type: application/json" -d "{\`"message\`": \`"Hello!\`"}"
  ```
  If `localhost` fails, use the container IP:
  ```powershell
  docker inspect <flask_container_name> | grep IPAddress
  curl -X POST http://172.17.0.2:8055/chat -H "Content-Type: application/json" -d "{\`"message\`": \`"Hello!\`"}"
  ```

### 5. Access the Application
- Open `http://localhost:8087` in a browser.
- Type a message, click **Send**, and view responses in the chat and history sidebar.
- Use the **Reset** button to clear the chat.

## Project Structure
```
flask_llm/
├── .env              # Environment variables (ignored by Git)
├── .gitignore        # Git ignore file
├── app.py            # Flask application (or web/app.py)
├── controllers/      # Request handlers
│   └── chat_controller.py
├── models/           # Data models
│   └── chat_request.py
├── services/         # Business logic
│   └── chat_service.py
├── frontend/         # React frontend
│   └── index.html
├── requirements.txt  # Python dependencies
├── Dockerfile        # Docker image for Flask
└── docker-compose.yml # Docker Compose configuration
```

## Development
- **Backend**: Modify `app.py`, `controllers/`, `services/`, or `models/`. Rebuild with `docker compose build`.
- **Frontend**: Edit `frontend/index.html`. Changes are reflected immediately (Nginx volume mount).
- **Environment**: Update `.env` for `OPENAI_API_KEY`. Restart containers:
  ```powershell
  docker compose down
  docker compose up -d
  ```

## License
MIT License. See [LICENSE](LICENSE) for details.