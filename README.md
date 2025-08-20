Patient Management System
📌 Project Overview

This project is a Patient Management System that allows users to manage patient records through a FastAPI backend and a Streamlit frontend.

The backend handles API requests and manages patient data.

The frontend provides a user-friendly interface for interacting with patient records.

The project follows a modular structure, making it easy to extend and maintain.

🛠️ Tech Stack

Backend: FastAPI, Uvicorn, Pydantic

Frontend: Streamlit

Database/Storage: JSON (can be extended to SQLite, PostgreSQL, or MongoDB)

Language: Python

Tools: Git, GitHub, VS Code

📂 Project Structure
patient-management-system
├── backend
│   ├── main.py          # FastAPI entry point
│   ├── models.py        # Data models
│   ├── schemas.py       # Pydantic schemas
│   ├── patients.json    # Patient data storage
│   └── requirements.txt # Backend dependencies
├── frontend
│   ├── app.py           # Streamlit frontend app
│   └── requirements.txt # Frontend dependencies
└── README.md

🚀 Features

Add, view, update, and delete patient records.

RESTful API endpoints for patient management.

Simple and interactive UI built with Streamlit.

Modular structure separating backend and frontend.

Easy setup and local deployment.

⚙️ Setup Instructions
1. Backend Setup
cd backend
pip install -r requirements.txt
uvicorn main:app --reload


API will be available at: http://localhost:8000

2. Frontend Setup
cd frontend
pip install -r requirements.txt
streamlit run app.py


Frontend will be available at: http://localhost:8501

3. Connecting Frontend and Backend

Ensure that the API URL in frontend/app.py points to the correct backend endpoint (e.g., http://localhost:8000/patients).

Use GET, POST, PUT, DELETE requests to interact with backend APIs.

4. Testing the Application

Open the frontend in a browser.

Add, view, update, and delete patient records.

🔮 Future Enhancements

Integration with SQL/NoSQL databases for persistent storage.

User authentication & role-based access (doctor, admin, staff).

Deployment on Docker / Cloud (AWS, Azure, GCP).

Advanced analytics dashboard for patient statistics.

🤝 Contribution

Contributions are welcome! To contribute:

Fork this repository

Create a new feature branch (git checkout -b feature-name)

Commit changes (git commit -m "Added new feature")

Push branch (git push origin feature-name)

Create a Pull Request
