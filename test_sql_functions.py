import sqlite3
import pytest

import sql_functions

def test_creation():
    """test table creation function"""
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()
    sql_functions.create_db(connection, "schema.sql")
    cursor.execute(
        ''' SELECT count(name) 
        FROM sqlite_master 
        WHERE type='table' AND name='dreams';''')
    results = cursor.fetchone()
    assert results[0] == 1
    connection.close()

def test_save():
    """test save function"""
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()
    sql_functions.save_image(connection, 'image1', 'description1', '2023-09-01', 'images')
    cursor.execute("""SELECT title, description, date, file_name FROM dreams;""")
    results = cursor.fetchall()
    for title, description, date, file_name in results:
        assert title == 'image1'
        assert description == 'description1'
        assert date == '2023-09-01'
        assert file_name == 'images/image1.jpg'
    sql_functions.save_image(connection, 'image2', 'description2', '2023-09-02', 'images')
    cursor.execute("""SELECT title FROM dreams;""")
    results = []
    for result in cursor.fetchall():
        results.append(result[0])
    assert results == ['image1', 'image2']
    connection.close()

def test_delete_image():
    """test delete one image function"""
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()
    sql_functions.delete_image(connection, 'images/image2.jpg')
    cursor.execute("""SELECT title FROM dreams;""")
    results = []
    for result in cursor.fetchall():
        results.append(result[0])
    assert results != ['image1', 'image2']
    connection.close()
    
def test_drop_table():
    """test drop table function"""
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()
    sql_functions.drop_table(connection)
    cursor.execute(
        ''' SELECT count(name) 
        FROM sqlite_master 
        WHERE type='table' AND name='dreams';''')
    results = cursor.fetchone()
    assert results[0] == 0
    connection.close()
