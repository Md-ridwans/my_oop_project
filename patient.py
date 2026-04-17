class Patient:
    """Base patient clss """
    def __init__(self,patient_name : str,paient_id:int):
        self.patient_name = patient_name
        self.Patient_id = paient_id
        self.bill_amount = 0.0

    def diagnose(self):
        return (f"[Diagnose] running general diagnose for {self.patient_name}")

    def treat(self):
        self.bill_amount = 500
        return (f"[Treat] providing general treatment for {self.patient_name}")
    
    def generate_report(self):
        # self.diagnose()
        # self.treat()
        return(f"[Bill ] Patient:{self.patient_name}|total : BDT {self.bill_amount}")
        # print("-"*70)
        
