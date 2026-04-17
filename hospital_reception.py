class HospitalReception:
    """hospital front desk with simulated method overloading """

    def admit_patient(self,patient_name:str,department:str ="General OPD",insurance_id = "SELF-PAY"):
        return (f"[Admitted]{patient_name} -> Dept: {department} | Insurance : {insurance_id}")
        