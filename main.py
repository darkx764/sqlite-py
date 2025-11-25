from classes.databases import databases
from classes.cli_prompter import menu
import classes.sqlite as conn

menu = menu() # init menu instance

def select_db():
    db = databases() # execute list databases menu
    s = db.show() # show list of db
    return s # return selected db

def main(db):
    while True:
        try:
            sql = conn.SQLiteDB(db) # execute connection on SQLite
            table = sql.tables() # show menu with list tables.
            while True: # loop into table state
                action = menu.select(
                    f"What you to do with {table} ? ^_^",
                    ['create','read','update','delete','< back']
                )
                match action:
                    case 'back': break 
                    case _:
                        sql(action, table)
                        
        except Exception as e:
            print(f"Exception occur in main file : {e}") # print error kalu jadi exception
            q = menu.confirm("An error occur. EXIT?") # confirmation message
            
            if q: 
                sql.disconnect()
                break

""" Execute the main function """  
sdb = select_db()
main(sdb)







