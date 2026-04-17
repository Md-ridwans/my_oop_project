from patient import Patient
class GeneralPatien(Patient):
    def __init__(self, patient_name, paient_id,symptoms:str):
        super().__init__(patient_name, paient_id)
        self.symptoms = symptoms
    def diagnose(self):
        return (f"[diagnose] Patient # {self.Patient_id} {self.patient_name}:",f"General checkup | Symptoms : {self.symptoms}")
    
    def treat(self):
        self.bill_amount = 800
        return (f"[treat] Prescribing medication and rest for {self.patient_name}")
        