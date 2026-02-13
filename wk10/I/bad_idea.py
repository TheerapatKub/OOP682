# ISP - Interface Segregation Principle 
# กล่าวว่า คลาสลูกไม่ควรถูกบังคับให้พึ่งพาอินเทอร์เฟซที่พวกเขาไม่ได้ใช้  

# Bad Idea of ISP Violation
class Machine:
    def print(self, document):
        pass
    def scan(self, document):
        pass
    def fax(self, document):
        pass

class OldPrinter(Machine): # เครื่องพิมพ์เก่า
    def print(self, document):
        print("Printing document...")
    def scan(self, document):
        raise NotImplementedError("This printer cannot scan.")
    def fax(self, document):
        raise NotImplementedError("This printer cannot fax.")   