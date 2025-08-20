from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import json
from typing import List, Dict

app = FastAPI()

# Load patient data from JSON file
def load_patients():
    with open("patients.json") as f:
        return json.load(f)

# Save patient data to JSON file
def save_patients(data):
    with open("patients.json", "w") as f:
        json.dump(data, f, indent=4)

# Patient model
class Patient(BaseModel):
    name: str
    city: str
    age: int
    gender: str
    height: float
    weight: float
    bmi: float
    verdict: str

# Get all patients
@app.get("/patients", response_model=Dict[str, Patient])
def get_patients():
    patients = load_patients()
    return patients

# Get a specific patient by ID
@app.get("/patients/{patient_id}", response_model=Patient)
def get_patient(patient_id: str):
    patients = load_patients()
    if patient_id not in patients:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patients[patient_id]

# Add a new patient
@app.post("/patients", response_model=Patient)
def add_patient(patient: Patient):
    patients = load_patients()
    patient_id = f"P{len(patients) + 1:03d}"
    patients[patient_id] = patient.dict()
    save_patients(patients)
    return JSONResponse(content=patients[patient_id], status_code=201)

# Update an existing patient
@app.put("/patients/{patient_id}", response_model=Patient)
def update_patient(patient_id: str, patient: Patient):
    patients = load_patients()
    if patient_id not in patients:
        raise HTTPException(status_code=404, detail="Patient not found")
    patients[patient_id] = patient.dict()
    save_patients(patients)
    return patients[patient_id]

# Delete a patient
@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: str):
    patients = load_patients()
    if patient_id not in patients:
        raise HTTPException(status_code=404, detail="Patient not found")
    del patients[patient_id]
    save_patients(patients)
    return JSONResponse(content={"detail": "Patient deleted"}, status_code=204)