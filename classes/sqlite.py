from classes.cli_prompter import menu
import sqlite3

class SQLiteDB:
    """ Simple sqlite connection manager class """
    def __init__(self, dbname):
        self.connection = None
        self.cursor = None
        self.dbname = f"databases/{dbname}" # db path name
        self.connect() # connect db

    def connect(self):
        """ make sqlite connection """
        try:
            # create connection 
            self.connection = sqlite3.connect(self.dbname)
            # cursor function for execute SQL statement
            self.cursor = self.connection.cursor()
        except Exception as e:
            print('exception error:', e)
        finally:
            pass

    def tables(self):
        """ List all available table in database """
        # checking if cursor instance not available
        if self.cursor is None:
            print("Error: Not connected to any database.")
            return []
        # sql query to get all data
        res = self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
        # fetch all tables
        tables = res.fetchall()
        return menu.select(f"Choose table in {self.dbname}", [table[0] for table in tables])

    def disconnect(self):
        """ close sqlite connection """
        self.connection.close()

    def columns(self, table):
        """ get selected table columns """
        return self.cursor.execute(f"SELECT name FROM PRAGMA_TABLE_INFO('{table}')")

    def create(self, table): 
        """ create a row """
        columns = self.columns(table)
        lists = []
        for column in columns:
            val = menu.text(f"{column[0]}: ")
            lists.append(val)
        print(lists)
        """ need to improve in term of saving follow with column datatype """
        # self.cursor.execute(f"INSERT INTO {table} ({column[0] for column in columns}) VALUES ({lists})")
    def read(self, table):
        """ fetch all data in table """
        query = self.cursor.execute(f"SELECT * FROM {table}")
        return menu.select(
            f"Data in {table}",
            query.fetchall()
        )

    def update(self, table):
        """ update selected row """
        row = self.read(table)
        columns = self.columns(table)
        column = menu.select(
            f"Select column to edit :",
            [tn[0] for tn in columns]
        )
        value = menu.text("Value to update :")
        self.cursor.execute(f"UPDATE {table} SET {column} = '{value}' WHERE id = {int(row[0])}")
        self.connection.commit()

    def delete(self, table):
        """ delete selected row """
        row = self.read(table)
        self.cursor.execute(f"DELETE FROM {table} WHERE id = {int(row[0])}")
        self.connection.commit()

    def __call__(self, method, table):
        """ method to redirect into CRUD """
        match method:
            case 'create':
                self.create(table)
            case 'read':
                self.read(table)
            case 'update':
                self.update(table)
            case 'delete':
                self.delete(table)