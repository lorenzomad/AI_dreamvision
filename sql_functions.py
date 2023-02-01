import sqlite3


def create_db(db_name, schema_file):
    """creates a db (if it doesn't exist) and schema"""
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    with open(schema_file, 'r') as rf:
        schema = rf.read()
    cursor.executescript(schema)
    connection.commit()
    connection.close()


    # cursor.execute("""insert into dreams (id, title, description, date, file_name)
    #                        values
    #                        (2, 'ciao', 'come va?', '2019-05-02', 'come_va.jpg');
    #                        """)


    # cursor.execute("""SELECT title FROM dreams""")
    # for row in cursor.fetchall():
    #     print(row)

