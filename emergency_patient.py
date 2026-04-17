from patient import Patient
class EmergencyPatient(Patient):
    def __init__(self, patient_name, paient_id,emergency_type):
        super().__init__(patient_name, paient_id)
        self.emergency_type = emergency_type
    
    def diagnose(self):
        return (f"[diagnose] Patient #{self.patient_name} Urgent Triage |emergency :{self.emergency_type}")
    
    def treat(self):
        self.bill_amount = 5000
        return (f"[treat] rushing {self.patient_name} to ER -> Iv Drip -> calling specialist")
    