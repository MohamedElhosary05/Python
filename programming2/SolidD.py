class MySQLDatabase:
    def connect(self):
        print("Connecting to MySQL")

class Application:
    def __init__(self):
        self.db = MySQLDatabase()

    def start(self):
        self.db.connect()


class Database:
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connecting to MySQL")

class Application:
    def __init__(self, db: Database):
        self.db = db

    def start(self):
        self.db.connect()

# استخدام:
db = MySQLDatabase()
app = Application(db)
app.start()
