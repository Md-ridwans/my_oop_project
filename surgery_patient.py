from patient import Patient
class SurgeryPatient(Patient):
    def __init__(self, patient_name, paient_id,surgery_type,surgeon_name):
        super().__init__(patient_name, paient_id)
        self.surgeon_Name = surgeon_name
        self.surgery_type = surgery_type

    def diagnose(self):
        return (f"[diagnose] Patien #{self.patient_name} pre surgical assesment for {self.surgery_type}")
    def treat(self):
        self.bill_amount = 250000
        return (f"[Treat]Preparing OT -> Anesthesia -> {self.surgeon_Name} performing {self.surgery_type}")
