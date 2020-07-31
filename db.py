import sqlite3


class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Address_Book (
                id INTEGER PRIMARY KEY,
                FirstName TEXT,
                LastName TEXT,
                Company TEXT,
                Phone INTEGER,
                Email TEXT,
                Address TEXT,
                Birthday TEXT
            )
        """)
        self.connection.commit()

    def fetch(self):
        self.cursor.execute("""
            SELECT * FROM Address_Book
        """)
        rows = self.cursor.fetchall()
        return rows

    def insert(self, firstName, lastName, company, phone, email, address, birthday):
        self.cursor.execute("""
            INSERT OR IGNORE INTO Address_Book VALUES (NULL,?, ?, ?, ?, ?, ?, ?)
        """, (firstName, lastName, company, phone, email, address, birthday))
        self.connection.commit()

    def remove(self, Id):
        self.cursor.execute("""
                    DELETE FROM Address_Book WHERE id=?
                """, (Id,))
        self.connection.commit()

    def update(self, Id, firstName, lastName, company, phone, email, address, birthday):
        self.cursor.execute("""
             UPDATE Address_Book SET 
             FirstName = ?,
             LastName = ?,
             Company = ?,
             Phone = ?,
             Email = ?,
             Address = ?,
             Birthday = ?
             WHERE id = ?
         """, (firstName, lastName, company, phone, email, address, birthday, Id))
        self.connection.commit()

    def search(self, firstName):
        self.cursor.execute("""
            SELECT * FROM Address_Book WHERE FirstName=?
        """, (firstName,))
        rows = self.cursor.fetchone()
        return rows

    def __del__(self):
        self.connection.close()


db = Database("try.sqlite")
db.insert("Fred", "Obeng", "None", "0545770712",
          "fredobeng@gmail.com", "Lashibi Comm. 19", "6/05/2000")
db.insert("Fred", "Obeng", "None", "0545770712",
          "fredobeng@gmail.com", "Lashibi Comm. 19", "6/05/2000")
db.insert("Fred", "Obeng", "None", "0545770712",
          "fredobeng@gmail.com", "Lashibi Comm. 19", "6/05/2000")
db.insert("Fred", "Obeng", "None", "0545770712",
          "fredobeng@gmail.com", "Lashibi Comm. 19", "6/05/2000")
db.insert("Fred", "Obeng", "None", "0545770712",
          "fredobeng@gmail.com", "Lashibi Comm. 19", "6/05/2000")
db.insert("Fred", "Obeng", "None", "0545770712",
          "fredobeng@gmail.com", "Lashibi Comm. 19", "6/05/2000")
db.insert("Fred", "Obeng", "None", "0545770712",
          "fredobeng@gmail.com", "Lashibi Comm. 19", "6/05/2000")
db.insert("Fred", "Obeng", "None", "0545770712",
          "fredobeng@gmail.com", "Lashibi Comm. 19", "6/05/2000")
db.insert("Fred", "Obeng", "None", "0545770712",
          "fredobeng@gmail.com", "Lashibi Comm. 19", "6/05/2000")
