import sqlite3

access_list = sqlite3.connect("etc/users/users_with_access.db", check_same_thread=False)
access_cursor = access_list.cursor()


class Users:
    """
    #? Table name = user
    #* Columns: username, accesskey(integer)

    """
    def __init__(self):
        self.create_table(True)
        self.users_with_access = []

    def create_table(self, true):
        self.true = true
        if self.true:
            access_cursor.execute("CREATE TABLE IF NOT EXISTS granteduser(username TEXT, access_code INTEGER)")
            access_list.commit()
        else:
            pass

    def access_list_entry(self, username, key):
        self.username = username
        self.key = key
        access_cursor.execute("SELECT * FROM user")
        access_cursor.execute("INSERT INTO granteduser(username, access_code) VALUES (?, ?)", (self.username, self.key))
        access_list.commit()

    def get_all_usernames(self, key):
        self.key = key
        access_cursor.execute(f"SELECT * FROM granteduser WHERE acccess_code={self.key}")
        for row in uvc.fetchall():
            self.users_with_access.append(row[0])

        return self.users_with_access


