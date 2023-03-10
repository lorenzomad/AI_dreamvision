""" module containing supporting sql functions to interact with the db.
before using these functions, create a working connection to the db.
these functions assume your schema uses dreams as table name."""

def create_db_from_file(connection, schema_file):
    """creates a schema on the connection"""
    cursor = connection.cursor()
    with open(schema_file, 'r') as rf:
        schema = rf.read()
    cursor.executescript(schema)
    
def create_db(connection):
    """creates a schema on the connection"""
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dreams(
    id INTEGER PRIMARY KEY,
    title TEXT,
    description TEXT,
    date DATE,
    file_name TEXT
);
""")



def save_image(connection, title, description, date, save_folder):
    """function to save the images to the db"""
    cursor = connection.cursor()
    cursor.execute(
        """insert into dreams (title, description, date, file_name)
        values (?,?,?,?);""", (title, description, date, save_folder + '/' + title.lower().replace(" ", "_") + '.jpg')
        )
    connection.commit()


def read_table(connection):
    """ function to read from a table and return the results"""
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM dreams;""")
    return cursor.fetchall()

def drop_table(connection):
    """function to drop a table"""
    cursor = connection.cursor()
    cursor.execute("""DROP TABLE IF EXISTS dreams;""")

def delete_image(connection, file_name):
    """deletes one image from the database"""
    cursor = connection.cursor()
    cursor.execute(
        """DELETE FROM dreams
        WHERE file_name=(?)""", (file_name,))
    connection.commit()
