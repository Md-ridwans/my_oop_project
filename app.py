import streamlit as st
from hospital_reception import HospitalReception
from general_patient import GeneralPatien
from emergency_patient import EmergencyPatient
from surgery_patient import SurgeryPatient
from api_calling import prescription_generator

st.title("Hospital Reception")
st.divider()
st.title("Patient info")

with st.container(border = True):
    st.title("Patient Information input")

    Patient_name = st.text_input("enter patient name")
    Patient_id = st.text_input("enter patient id")
    Department = st.text_input("patient department")
    Insurance_id = st.text_input("patient insurance id")

#hospital reception

with st.container(border= True):
    st.markdown(
    "<h2 style='color: green;'>Patient Confirmation Receipt</h2>",
    unsafe_allow_html=True
)
    recepton = HospitalReception()
    
    if st.button("Admit Patient"):
        result = recepton.admit_patient(Patient_name,Department,Patient_id)
        st.success(result)
    
#patient situation


selected = st.selectbox(
    "select",
    ["General Patient","Emergency Patient","Surgery Patient"],
    index = None
)



with st.container(border = True):

    if selected == "General Patient":
        Symptoms = st.text_input("input symtomes")
        if st.button("Generate Patient Report"):
            patient = GeneralPatien(Patient_name, Patient_id, Symptoms)

            result = [
                patient.diagnose(),
                patient.treat(),
                patient.generate_report()
            ]

            for r in result:
                st.success(r)

        #container
    if selected == "Emergency Patient":
        Emtype = st.text_input("enter patient emergency type")
        Patient = EmergencyPatient(Patient_name,Patient_id,Emtype)
            # if button("Patien situation"):
        if st.button("Generate Patient Report"):
            patient = EmergencyPatient(Patient_name, Patient_id, Emtype)

            result = [
                patient.diagnose(),
                patient.treat(),
                patient.generate_report()
            ]

            for r in result:
                st.success(r)

        #container 
    if selected == "Surgery Patient":
        surgr_typ = st.text_input("enter surgery type")
        surgen_nmae = st.text_input("enter Surgeon Name")
        if st.button("Generate Patient Report"):
            patient = SurgeryPatient(Patient_name, Patient_id,surgr_typ,surgen_nmae)

            result = [
                patient.diagnose(),
                patient.treat(),
                patient.generate_report()
            ]

            for r in result:
                st.success(r)




with st.container(border = True):
    st.title("AI Doctor Prescription")
    if st.button("Generate Prescription"):
        with st.container(border = True):
            if selected == "General Patient":
                response = prescription_generator(Symptoms)
                st.markdown(response.text)
            if selected == "Emergency Patient":
                response = prescription_generator(Emtype)
                st.markdown(response.text)
            if selected =="Surgery Patient":
                response = prescription_generator(surgr_typ)
                st.markdown(response.text)



