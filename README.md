# Patient Management System

## Project Overview
This project is a Patient Management System that allows users to manage patient records through a FastAPI backend and a Streamlit frontend. The backend handles API requests and manages patient data, while the frontend provides a user-friendly interface for interacting with the patient records.

## Project Structure
```
patient-management-system
├── backend
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── patients.json
│   └── requirements.txt
├── frontend
│   ├── app.py
│   └── requirements.txt
└── README.md
```

## Setup Instructions for Patient Management System

1. **Backend Setup**:
   - Navigate to the `backend` directory.
   - Install the required packages using pip:
     ```
     pip install -r requirements.txt
     ```
   - Run the FastAPI application:
     ```
     uvicorn main:app --reload
     ```
   - The API will be available at `http://localhost:8000`.

2. **Frontend Setup**:
   - Navigate to the `frontend` directory.
   - Install the required packages using pip:
     ```
     pip install -r requirements.txt
     ```
   - Run the Streamlit application:
     ```
     streamlit run app.py
     ```
   - The frontend will be available at `http://localhost:8501`.

3. **Connecting Frontend and Backend**:
   - Ensure that the API URL in `frontend/app.py` points to the correct backend endpoint (e.g., `http://localhost:8000/patients`).
   - Use the appropriate HTTP methods (GET, POST, PUT, DELETE) in the frontend to interact with the backend API for managing patient records.

4. **Testing the Application**:
   - Open a web browser and navigate to the frontend URL.
   - Use the interface to add, view, and update patient records, which will interact with the backend API.