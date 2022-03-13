import sqlite3

uconn = sqlite3.connect("etc/users/users.db", check_same_thread=False)
uc = uconn.cursor()


class Users:
    """
    #? Table name = user
    #* Columns: email, password, username, website

    """
    def __init__(self):
        self.create_table(True)
        self.column1 = []

    def create_table(self, true):
        self.true = true
        if self.true:
            uc.execute("CREATE TABLE IF NOT EXISTS user(email TEXT, password TEXT, username TEXT, website TEXT)")
            uconn.commit()
        else:
            pass

    def user_entry(self, email, password, username, website):
        self.email = email
        self.password = password
        self.username = username
        self.website = website
        uc.execute("SELECT * FROM user")
        uc.execute("INSERT INTO user(email, password, username, website) VALUES (?, ?, ?, ?)", (self.email, self.password, self.username, self.website))
        uconn.commit()

    def get_username(self, email):
        self.email = str(email)
        uc.execute(f"SELECT * FROM user WHERE email={self.email}")
        for row in uc.fetchall():
            if self.email == row[0]:
                return row[2]
            else:
                return False

    def get_webiste(self, email):
        self.email = email
        uc.execute(f"SELECT * FROM user WHERE email={self.email}")
        for row in uc.fetchall():
            if self.email == row[0]:
                return row[3]
            else:
                return False

    def get_password(self, email):
        self.email == email
        uc.execute(f"SELECT * FROM user where email={self.email}")
        for row in uc.fetchall():
            if self.email == row[0]:
                return row[1]
            else:
                return False

    def get_email(self, username):
        self.username = username
        uc.execute(f"SELECT * FROM user where username={self.username}")
        for row in uc.fetchall():
            if self.username == row[2]:
                return row[0]
            else:
                return False
