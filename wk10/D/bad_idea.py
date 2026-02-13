# DIP = Dependency Inversion Principle
# กล่าวว่า โมดูลระดับสูงไม่ควรพึ่งพาโมดูลระดับต่ำ   

# Bad Idea of DIP Violation
class App:
    def __init__(self):
        self.database = MySQLDatabase()  # ผิดหลัก DIP เพราะ App พึ่งพา MySQLDatabase โดยตรง
    def save_data(self, data):
        self.database.save(data)

class MySQLDatabase:
    def save(self, data):
        print("Saving data to MySQL database...")

app = App()
app.save_data("Some important data")