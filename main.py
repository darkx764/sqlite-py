from classes.databases import databases
from classes.cli_prompter import menu
from classes.file import file_management as f
import classes.sqlite as conn

def select_db():
    db = databases() # execute list databases menu
    s = db.show() # show list of db

    f.save('select_db') # save user state
    return s # return selected db

def main(db):
    while True:
        try:
            sql = conn.SQLiteDB(db) # execute connection on SQLite
            table = sql.tables() # show menu with list tables.
            f.save('select_table') # save user state
            while True: # loop into table state
                action = menu.select(
                    f"What you to do with {table} ? ^_^",
                    ['< back','create','read','update','delete']
                )
                f.save('action') # save user state
                match action:
                    case '< back': 
                        break
                    case _:
                        sql(action, table)
                    
        except Exception as e:
            print(f"Exception occur in main file : {e}") # print error kalu jadi exception
            q = menu.confirm("An error occurred. EXIT?") # confirmation message
            
            if q: 
                sql.disconnect()
                break

""" Execute the main function """  
sdb = select_db()
main(sdb)







