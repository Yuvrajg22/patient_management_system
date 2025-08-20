import streamlit as st
import requests

API_URL = "http://localhost:8000/patients"

st.title("Patient Management System")
st.markdown("Manage patient records below:")

def fetch_patients():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error fetching patient data: {response.text}")
            return {}
    except Exception as e:
        st.error(f"Error connecting to backend: {e}")
        return {}

def add_patient(patient_data):
    try:
        response = requests.post(API_URL, json=patient_data)
        if response.status_code in (200, 201):
            st.success("Patient added successfully!")
        else:
            st.error(f"Error adding patient: {response.text}")
    except Exception as e:
        st.error(f"Error connecting to backend: {e}")

def update_patient(patient_id, patient_data):
    try:
        response = requests.put(f"{API_URL}/{patient_id}", json=patient_data)
        if response.status_code == 200:
            st.success("Patient updated successfully!")
        else:
            st.error(f"Error updating patient: {response.text}")
    except Exception as e:
        st.error(f"Error connecting to backend: {e}")

def calculate_bmi(weight, height):
    if height > 0:
        return round(weight / (height * height), 2)
    return 0

def get_verdict(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Display existing patients
patients = fetch_patients()
if patients:
    st.subheader("Existing Patients")
    if isinstance(patients, list):
        patients = {str(i): p for i, p in enumerate(patients)}
    for patient_id, patient in patients.items():
        st.write(f"ID: {patient_id}, Name: {patient['name']}, Age: {patient['age']}, City: {patient['city']}")

# Input fields for adding a new patient
st.subheader("Add New Patient")
name = st.text_input("Name")
city = st.text_input("City")
age = st.number_input("Age", min_value=1, max_value=120, step=1)
gender = st.selectbox("Gender", options=["male", "female", "other"])
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, step=0.01)
weight = st.number_input("Weight (kg)", min_value=1.0, step=0.1)

if st.button("Add Patient"):
    # Check all required fields
    if all([name.strip(), city.strip(), age, height, weight]):
        bmi = calculate_bmi(weight, height)
        verdict = get_verdict(bmi)
        patient_data = {
            "name": name,
            "city": city,
            "age": int(age),
            "gender": gender,
            "height": float(height),
            "weight": float(weight),
            "bmi": bmi,
            "verdict": verdict
        }
        add_patient(patient_data)
    else:
        st.error("Please fill in all required fields.")

# Input fields for updating an existing patient
st.subheader("Update Existing Patient")
update_patient_id = st.text_input("Patient ID to Update")
if update_patient_id:
    patient_data = fetch_patients().get(update_patient_id)
    if patient_data:
        name_upd = st.text_input("Update Name", value=patient_data['name'], key="update_name")
        city_upd = st.text_input("Update City", value=patient_data['city'], key="update_city")
        age_upd = st.number_input("Update Age", min_value=1, max_value=120, value=patient_data['age'], step=1, key="update_age")
        gender_upd = st.selectbox("Update Gender", options=["male", "female", "other"], index=["male", "female", "other"].index(patient_data['gender']), key="update_gender")
        height_upd = st.number_input("Update Height (m)", min_value=0.5, max_value=2.5, value=patient_data['height'], step=0.01, key="update_height")
        weight_upd = st.number_input("Update Weight (kg)", min_value=1.0, value=patient_data['weight'], step=0.1, key="update_weight")

        if st.button("Update Patient"):
            if all([name_upd.strip(), city_upd.strip(), age_upd, height_upd, weight_upd]):
                bmi = calculate_bmi(weight_upd, height_upd)
                verdict = get_verdict(bmi)
                updated_data = {
                    "name": name_upd,
                    "city": city_upd,
                    "age": int(age_upd),
                    "gender": gender_upd,
                    "height": float(height_upd),
                    "weight": float(weight_upd),
                    "bmi": bmi,
                    "verdict": verdict
                }
                update_patient(update_patient_id, updated_data)
            else:
                st.error("Please fill in all required fields.")
    else:
        st.error("Patient ID not found.")