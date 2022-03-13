import sqlite3

conn = sqlite3.connect("memory.db", check_same_thread=False)
c = conn.cursor()


class MemoryUnit:
    """
                                        METADATA OF CLASS
    ---------------------------------------------------------------------------------------
    Connection pool: sqlite3 :: conn = sqlite3.connect("memory.db")
    ---------------------------------------------------------------------------------------
    Cursor of Database: sqlite3 :: c = conn.cursor()
    ---------------------------------------------------------------------------------------
    Total methods in class : MemoryUnit :: 3 methods, 1 initialisation method
    ---------------------------------------------------------------------------------------
    Server overdrive : Memory end :: conn.commit() ::: c.close() ::: conn.close()
    ---------------------------------------------------------------------------------------

    =======================================================================================
    # Method: create_table(self, true): if there is no table already created, create one, else pass.
    # using SQL for creating table-- CREATE TABLE IF NOT EXISTS memoryUnit(name TEXT, date TEXT, entry TEXT)
    # and creating 2 coloumns for question and answer whose data type is string
    #
    # Method: data_entry(self, name, dates, entry): takes the question and answer, so that we can
    # assign question along with answer in the same row. SQL used.
    # "INSERT INTO memoryUnit (name, dates, entry) VALUES (?, ?, ?)", (self.name, self.dates, self.entry)
    =======================================================================================

    """
    def __init__(self):
        self.column1 = []
        self.create_table(True)

    def create_table(self, true):
        self.true = true
        if self.true:
            try:
                c.execute("CREATE TABLE IF NOT EXISTS memoryUnit(user TEXT, password TEXT)")
                conn.commit()
            except Exception as e:
                print(e)
        else:
            pass

    def data_entry(self, user, pw):
        self.user = user
        self.pw = pw
        try:
            c.execute("INSERT INTO memoryUnit (user, password) VALUES (?, ?)", (self.user, self.pw))
            conn.commit()
        except Exception as e:
            print(e)


