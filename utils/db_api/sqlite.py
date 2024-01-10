import sqlite3

class DBManager:
    def  __init__(self):
        self.conn = sqlite3.connect('shop.db')
        self.cursor = self.conn.cursor()


    def get_user(self, chat_id):
        query = f"select * from users where chat_id = {chat_id}"
        return self.cursor.execute(query).fetchone()
    

    def insert_user(self, data : dict):
        full_name = data['full_name']
        login = data['login']
        password = data['password']
        phone_number = data['phone_number']
        chat_id = data['chat_id']


        query = "insert into users (fullname, login, password, chat_id, phone_number)  values (?,?,?,?,?)"
        values = (full_name, login, password, chat_id, phone_number)


        self.cursor.execute(query, values)
        self.conn.commit()
        return True
    
class TableManager:
    def __init__(self):
        self.conn = sqlite3.connect('shop.db')
        self.conn.commit() 


    def create_table(self):
        query = """CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id INTEGER,
        phone_number TEXT NOT NULL,
        login TEXT NOT NULL,
        password TEXT NOT NULL,
        full_name TEXT NOT NULL
        )
        """    
        self.cursor.execute(query)
        self.conn.commit()



table_manager = TableManager()
table_manager.create_table()