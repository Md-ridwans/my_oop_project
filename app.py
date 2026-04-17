

import streamlit as st
from hospital_reception import HospitalReception
from patient import Patient
from general_patient import GeneralPatient
from emergency_patient import EmergencyPatient
from surgery_patient import SurgeryPatient
from api_calling import prescription_generator

st.set_page_config(page_title="Hospital Management", layout="centered")
st.title("🏥 Hospital Reception System")
st.divider()

# ====================== Patient Information ======================
with st.container(border=True):
    st.subheader("Patient Information")
    
    col1, col2 = st.columns(2)
    with col1:
        patient_name = st.text_input("Patient Name", placeholder="Enter full name")
        patient_id = st.text_input("Patient ID", placeholder="e.g. P-001")
    with col2:
        department = st.text_input("Department", value="General OPD")
        insurance_id = st.text_input("Insurance ID", value="SELF-PAY")

# ====================== Admit Patient ======================
with st.container(border=True):
    st.markdown("<h3 style='color: green;'>Patient Confirmation Receipt</h3>", unsafe_allow_html=True)
    
    reception = HospitalReception()
    
    if st.button("Admit Patient", type="primary"):
        if not patient_name or not patient_id:
            st.error("Please enter Patient Name and Patient ID")
        else:
            result = reception.admit_patient(patient_name, department, insurance_id)
            st.success(result)

# ====================== Patient Type Selection ======================
st.subheader("Select Patient Type")
selected = st.selectbox(
    "Choose patient category",
    ["General Patient", "Emergency Patient", "Surgery Patient"],
    index=None,
    placeholder="Select one..."
)

# ====================== Patient Processing ======================
with st.container(border=True):
    if selected == "General Patient":
        symptoms = st.text_input("Enter Symptoms", placeholder="e.g. Fever, cough, headache")
        
        if st.button("Generate General Patient Report", type="primary"):
            if not symptoms:
                st.warning("Please enter symptoms")
            else:
                patient = GeneralPatient(patient_name, patient_id, symptoms)
                st.success(patient.diagnose())
                st.success(patient.treat())
                st.success(patient.generate_report())

    elif selected == "Emergency Patient":
        emergency_type = st.text_input("Emergency Type", placeholder="e.g. Cardiac Arrest, Severe Bleeding")
        
        if st.button("Generate Emergency Report", type="primary"):
            if not emergency_type:
                st.warning("Please enter emergency type")
            else:
                patient = EmergencyPatient(patient_name, patient_id, emergency_type)
                st.success(patient.diagnose())
                st.success(patient.treat())
                st.success(patient.generate_report())

    elif selected == "Surgery Patient":
        surgery_type = st.text_input("Surgery Type", placeholder="e.g. Appendectomy")
        surgeon_name = st.text_input("Surgeon Name", placeholder="Dr. Khan")
        
        if st.button("Generate Surgery Report", type="primary"):
            if not surgery_type or not surgeon_name:
                st.warning("Please fill Surgery Type and Surgeon Name")
            else:
                patient = SurgeryPatient(patient_name, patient_id, surgery_type, surgeon_name)
                st.success(patient.diagnose())
                st.success(patient.treat())
                st.success(patient.generate_report())

# ====================== AI Prescription ======================
with st.container(border=True):
    st.subheader("🩺 AI Doctor Prescription")
    
    if st.button("Generate AI Prescription", type="primary"):
        if not selected:
            st.error("Please select a patient type first")
        else:
            with st.spinner("Generating prescription..."):
                try:
                    if selected == "General Patient":
                        input_text = symptoms if 'symptoms' in locals() else ""
                    elif selected == "Emergency Patient":
                        input_text = emergency_type if 'emergency_type' in locals() else ""
                    else:
                        input_text = surgery_type if 'surgery_type' in locals() else ""
                    
                    if input_text:
                        response = prescription_generator(input_text)
                        st.markdown(response.text)
                    else:
                        st.warning("No input data available for prescription")
                except Exception as e:
                    st.error(f"Failed to generate prescription: {e}")

st.caption("Hospital Management System | Built with OOP + Gemini AI")
