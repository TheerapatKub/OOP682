# DIP = Dependency Inversion Principle
# กล่าวว่า โมดูลระดับสูงไม่ควรพึ่งพาโมดูลระดับต่ำ 

# Good Idea of DIP Adherence
from abc import ABC, abstractmethod

class Database(ABC): # Abstract Base Class
    @abstractmethod
    def save(self, data):
        pass

class MySQLDatabase(Database):
    def save(self, data):
        print("Saving data to MySQL database...")

class PostgreSQLDatabase(Database):
    def save(self, data):
        print("Saving data to PostgreSQL database...")

class App:
    def __init__(self, database: Database):
        # App พึ่งพาอินเทอร์เฟซ Database 
        # แทนที่จะพึ่งพา MySQLDatabase โดยตรง
        self.database = database  
    
    def save_data(self, data):
        self.database.save(data)