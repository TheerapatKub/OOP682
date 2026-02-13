# S = SRP = Single Responsibility Principle

# Bad Idea: A class that handles multiple responsibilities
class ReportGenerator:

    def __init__(self, data):
        self.data = data
    
    def generate_pdf(self):
        pass

    def generate_excel(self):
        pass

    def send_email(self, recipient):
        pass
