import sqlite3
import datetime

vconn = sqlite3.connect("etc/taskmanager/vuser.db", check_same_thread=False)
vc = vconn.cursor()

#! Needs more improvent.
#? Quick Terms:
#? Table name: vHost
#? params into table: serverID, serverName, serverDescription, userID
#? total entries: 4
#? Class name: VirtualUnit
id_container = []

class VirtualUnit:
    """

    Builds virtual rooms for new notebooks. Contain all methods to control virtual-notebooks. 
    Can retrieve data, store data, and much more

    """
    def __init__(self):
        self.column1 = []
        self.create_table(True)


    def create_table(self, true):
        self.true = true
        if self.true:
            vc.execute("CREATE TABLE IF NOT EXISTS vHost(serverID INTEGER, serverName TEXT, serverDescription TEXT, date TEXT, host TEXT, memberAccessCode TEXT)")
            vconn.commit()
        else:
            pass


    def new_notebook(self, serverID, serverName, serverDescription, host, memberAccessCode):
        self.serverID = serverID
        self.serverName = serverName
        self.serverDescription = serverDescription
        self.date =  "at " + str(datetime.datetime.now().strftime("%H:%M:%S")) + " on " + str(
			datetime.datetime.now().day) + "/" + str(
			datetime.datetime.now().month) + "/" + str(
			datetime.datetime.now().year)
        self.host = host
        self.memberAccessCode = memberAccessCode
        vc.execute("INSERT INTO vHost (serverID, serverName, serverDescription, date, host, memberAccessCode) VALUES (?, ?, ?, ?, ?, ?)", (self.serverID, self.serverName, self.serverDescription, self.date, self.host, self.memberAccessCode))
        vconn.commit()


    def get_notebook_id(self, notebookname):
        self.notebookname = notebookname.lower().replace(" ", "")
        vc.execute(f"SELECT * FROM vHost WHERE serverName = {self.notebookname}")
        for row in vc.fetchall():
            if self.notebookname == row[1]:
                return row[0]
            else:
                return "Notebook not found!!"


    def get_notebook_name(self, id):
        self.id = id
        vc.execute(f"SELECT * FROM vHost WHERE serverID = {self.id}")
        for i in vc.fetchall():
            if self.id == row[0]:
                return row[1]
            else:
                return "Notebook not found!!"


    def get_notebook_description(self, id):
        self.id = id
        vc.execute(f"SELECT * FROM vHost WHERE serverID = {self.id}")
        for i in vc.fetchall():
            if self.id == row[0]:
                return row[2]
            else:
                return "Notebook not found!!"


    def get_notebook_date(self, id):
        self.id = id
        vc.execute(f"SELECT * FROM vHost WHERE serverID = {self.id}")
        for i in vc.fetchall():
            if self.id == row[0]:
                return row[3]
            else:
                return "Notebook not found!!"


    def get_notebook_host_name(self, id):
        self.id = id
        vc.execute(f"SELECT * FROM vHost WHERE serverID = {self.id}")
        for i in vc.fetchall():
            if self.id == row[0]:
                return row[4]
            else:
                return "Notebook not found!!"


    def get_notebook_member_access_code(self, id):
        self.id = id
        vc.execute(f"SELECT * FROM vHost WHERE serverID = {self.id}")
        for i in vc.fetchall():
            if self.id == row[0]:
                return row[5]
            else:
                return "Notebook not found!!"


vunit = VirtualUnit()