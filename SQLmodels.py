import sqlite3
from sqlite3 import Error


class Todos:

    def create_database():
        #Connect/crete databazse
        conn = sqlite3.connect( 'todos.db')
        #Create a cursor
        c = conn.cursor()
        # Create a Table
        c.execute(""" CREATE TABLE todos (
            title varchar(255),
            description varchar(255),
            done Boolean
            )""")
        conn.commit()
        conn.close()

    def  create_connection(db_file):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to {db_file}, sqlite version: {sqlite3.version}")
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()


    def print_all():
        conn = sqlite3.connect( 'todos.db')
        c = conn.cursor()
        # Query the database
        c.execute( "SELECT rowid, * FROM todos" )
        c.fetchall()
        items = c.fetchall()
        for item in items:
            print(item)


    def add_record(values):             #values to krotka z form
        conn = sqlite3.connect( 'todos.db')
        sql = '''INSERT INTO todos (title,description,done)
                VALUES(?,?,?)'''
        c = conn.cursor()
        c.execute ( "INSERT INTO todos VALUES (?,?,?)" (sql,values) )
        conn.commit()
        conn.close()




    def delete(id):
        conn = sqlite3.connect( 'todos.db')
        c = conn.cursor()
        c.execute ( "DELETE from todos WHERE rowid = (?)", id )
        conn.commit()
        conn.close()
