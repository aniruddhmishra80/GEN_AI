# FastAPI Product Management Application

A full-stack product management application built with FastAPI backend and React frontend.

## Project Structure

```
fastapi/
├── main.py              # FastAPI app with CRUD endpoints
├── models.py            # Pydantic data models
├── pyproject.toml       # Project metadata
├── requirements.txt     # Python backend dependencies
└── frontend/            # React frontend application
    ├── public/
    ├── src/
    ├── package.json
    └── package-lock.json
```

## Running the Backend

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload --port 8000
   ```

3. Access the interactive API docs at `http://localhost:8000/docs`.

## Running the Frontend

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```
