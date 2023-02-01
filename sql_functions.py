import sqlite3


def create_db(connection, schema_file):
    """creates a schema on the connection"""
    cursor = connection.cursor()
    with open(schema_file, 'r') as rf:
        schema = rf.read()
    cursor.executescript(schema)
    

def save_image(connection, title, description, date, save_folder):
    cursor = connection.cursor()
    cursor.execute(
        """insert into dreams (title, description, date, file_name)
        values (?,?,?,?)""", (title, description, date, save_folder + '/' + title.replace(" ", "_") + '.jpg')
        )
    connection.commit()


def read_table(connection):
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM dreams""")
    for row in cursor.fetchall():
        print(row)

