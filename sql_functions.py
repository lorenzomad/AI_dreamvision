import sqlite3
# before using these functions, create a working connection to the db.
# these functions assume your schema uses dreams as table name.

def create_db(connection, schema_file):
    """creates a schema on the connection"""
    cursor = connection.cursor()
    with open(schema_file, 'r') as rf:
        schema = rf.read()
    cursor.executescript(schema)
    

def save_image(connection, title, description, date, save_folder):
    """function to save the images to the db"""
    cursor = connection.cursor()
    cursor.execute(
        """insert into dreams (title, description, date, file_name)
        values (?,?,?,?);""", (title, description, date, save_folder + '/' + title.replace(" ", "_") + '.jpg')
        )
    connection.commit()


def read_table(connection):
    """ function to read from a table"""
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM dreams;""")
    for row in cursor.fetchall():
        print(row)

def drop_table(connection):
    """function to drop a table"""
    cursor = connection.cursor()
    cursor.execute("""DROP TABLE IF EXISTS dreams;""")
