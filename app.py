
import streamlit as st
from hospital_reception import HospitalReception
from general_patient import GeneralPatien
from emergency_patient import EmergencyPatient
from surgery_patient import SurgeryPatient
from api_calling import prescription_generator

st.title("Hospital Reception")
st.divider()
st.title("Patient info")

with st.container(border=True):
    st.title("Patient Information input")

    Patient_name = st.text_input("enter patient name")
    Patient_id = st.text_input("enter patient id")
    Department = st.text_input("patient department")
    Insurance_id = st.text_input("patient insurance id")

# Hospital Reception
with st.container(border=True):
    st.markdown(
        "<h2 style='color: green;'>Patient Confirmation Receipt</h2>",
        unsafe_allow_html=True
    )
    recepton = HospitalReception()
    
    if st.button("Admit Patient"):
        if Patient_name and Patient_id:
            result = recepton.admit_patient(Patient_name, Department, Insurance_id)
            st.success(result)
        else:
            st.error("Patient Name and Patient ID are required!")

# Patient Type Selection
selected = st.selectbox(
    "select",
    ["General Patient", "Emergency Patient", "Surgery Patient"],
    index=None
)

with st.container(border=True):
    if selected == "General Patient":
        Symptoms = st.text_input("input symtomes")
        if st.button("Generate Patient Report"):
            if Patient_name and Patient_id and Symptoms:
                patient = GeneralPatien(Patient_name, Patient_id, Symptoms)
                result = [
                    patient.diagnose(),
                    patient.treat(),
                    patient.generate_report()
                ]
                for r in result:
                    st.success(r)
            else:
                st.warning("Please fill Patient Name, ID and Symptoms")

    if selected == "Emergency Patient":
        Emtype = st.text_input("enter patient emergency type")
        if st.button("Generate Patient Report"):
            if Patient_name and Patient_id and Emtype:
                patient = EmergencyPatient(Patient_name, Patient_id, Emtype)
                result = [
                    patient.diagnose(),
                    patient.treat(),
                    patient.generate_report()
                ]
                for r in result:
                    st.success(r)
            else:
                st.warning("Please fill all required fields")

    if selected == "Surgery Patient":
        surgr_typ = st.text_input("enter surgery type")
        surgen_nmae = st.text_input("enter Surgeon Name")
        if st.button("Generate Patient Report"):
            if Patient_name and Patient_id and surgr_typ and surgen_nmae:
                patient = SurgeryPatient(Patient_name, Patient_id, surgr_typ, surgen_nmae)
                result = [
                    patient.diagnose(),
                    patient.treat(),
                    patient.generate_report()
                ]
                for r in result:
                    st.success(r)
            else:
                st.warning("Please fill all required fields")

# AI Prescription Section
with st.container(border=True):
    st.title("AI Doctor Prescription")
    if st.button("Generate Prescription"):
        if not selected:
            st.error("Please select a patient type first!")
        else:
            with st.spinner("Generating AI prescription..."):
                try:
                    if selected == "General Patient":
                        response = prescription_generator(Symptoms)
                    elif selected == "Emergency Patient":
                        response = prescription_generator(Emtype)
                    elif selected == "Surgery Patient":
                        response = prescription_generator(surgr_typ)
                    else:
                        response = None
                    
                    if response:
                        st.markdown(response.text)
                    else:
                        st.warning("No input data for prescription")
                except Exception as e:
                    st.error(f"Error generating prescription: {str(e)}")
