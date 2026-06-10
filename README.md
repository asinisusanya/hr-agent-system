# HR Multi-Agent System

An AI-powered Human Resource assistance platform that uses LangGraph, Gemini AI, FastAPI, and React to intelligently classify employee requests, route them to specialized HR agents, and manage conversational memory.

## Features

* AI-based intent classification using Gemini 2.5 Flash
* Multi-agent request routing with LangGraph
* Specialized HR agents:

  * Leave Agent
  * Scheduling Agent
  * Compliance Agent
  * Clarification Agent
* Short-Term Memory (STM)
* Long-Term Memory (LTM)
* Audit Logging
* Interactive React Dashboard
* Real-time request processing and monitoring

## System Architecture

```text
Employee Request
       │
       ▼
Intent Classification (Gemini)
       │
       ▼
LangGraph Router
       │
 ┌─────┼─────┬──────────┬─────────────┐
 ▼     ▼     ▼          ▼
Leave Scheduling Compliance Clarification
Agent    Agent      Agent      Agent
       │
       ▼
Memory Manager
       │
       ▼
STM + LTM + Audit Logs
```

## Technology Stack

### Backend

* FastAPI
* LangGraph
* LangChain
* Gemini 2.5 Flash
* SQLAlchemy
* SQLite

### Frontend

* React
* Vite
* Axios

### Database

* SQLite

## Project Structure

```text
hr-agent-system/
│
├── agents/
├── app/
├── audit/
├── database/
├── frontend/
├── graph/
├── memory/
├── router/
├── utils/
│
├── main.py
├── requirements.txt
├── README.md
└── .env
```

## Installation

### Clone Repository

```bash
git clone https://github.com/asinisusanya/hr-agent-system.git

cd hr-agent-system
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

## Running the Backend

```bash
uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

## Running the Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

## API Endpoints

| Method | Endpoint              | Description              |
| ------ | --------------------- | ------------------------ |
| GET    | /health               | Health check             |
| POST   | /request              | Process employee request |
| GET    | /memory/{user_id}     | Retrieve user memory     |
| DELETE | /memory/{user_id}     | Clear all memory         |
| DELETE | /memory/stm/{user_id} | Clear STM                |
| DELETE | /memory/ltm/{user_id} | Clear LTM                |
| GET    | /audit                | Retrieve audit logs      |

## Memory Management

### Short-Term Memory (STM)

Stores recent conversations and interactions.

Examples:

* Schedule a meeting tomorrow.
* I need leave next Monday.

### Long-Term Memory (LTM)

Stores significant user preferences and recurring information.

Examples:

* I prefer morning meetings.
* I prefer remote work.

## Workflow

1. Employee submits a request.
2. Gemini classifies the intent.
3. LangGraph routes the request to the appropriate HR agent.
4. Agent generates a response.
5. Memory manager updates STM and LTM.
6. Audit logs are recorded.
7. Results are displayed on the dashboard.

## Author

Asini Susanya
