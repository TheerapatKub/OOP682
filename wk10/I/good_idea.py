# ISP - Interface Segregation Principle 
# กล่าวว่า คลาสลูกไม่ควรถูกบังคับให้พึ่งพาอินเทอร์เฟซที่พวกเขาไม่ได้ใช้  

# Good Idea of ISP Adherence
from abc import abstractmethod

class Printer:
    @abstractmethod
    def print(self, document):
        pass
class Scanner:
    @abstractmethod
    def scan(self, document):
        pass
class Fax:
    @abstractmethod
    def fax(self, document):
        pass
class OldPrinter(Printer): # เครื่องพิมพ์เก่า
    def print(self, document):
        print("Printing document...")
# เครื่องพิมพ์มัลติฟังก์ชัน
class MultiFunctionPrinter(Printer, Scanner, Fax): 
    def print(self, document):
        print("Printing document...")
    def scan(self, document):
        print("Scanning document...")
    def fax(self, document):
        print("Faxing document...")