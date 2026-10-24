# LeadPilot — AI-Powered Lead Qualification MCP Server

LeadPilot is a lead qualification prototype built with Python,
FastMCP, and FastAPI.

## Features

- Scores sales leads using budget, interest, and urgency.
- Classifies leads as High, Medium, or Low priority.
- Recommends a follow-up action.
- Exposes lead qualification through an MCP tool.
- Provides a REST API endpoint.
- Validates inputs and rejects invalid requests.

## Tech Stack

- Python
- FastMCP
- FastAPI
- Pydantic
- Uvicorn

## Project Files

- `lead_logic.py` — lead scoring and validation logic
- `mcp_server.py` — MCP server and tool
- `api.py` — FastAPI application
- `requirements.txt` — required packages

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the API

From the project directory:

```bash
uvicorn api:app --reload
```

Open `http://127.0.0.1:8000/docs` in your browser
to test the API.

## API Endpoint

`POST /qualify-lead`

Example request:

```json
{
  "customer_name": "Aisha",
  "budget": 60000,
  "interest_level": "hot",
  "urgency": "high"
}
```

## Current Scope

Lead scoring uses predefined rules. The project currently
provides an MCP tool and a REST API; LLM-based autonomous
decision-making is not yet implemented.
