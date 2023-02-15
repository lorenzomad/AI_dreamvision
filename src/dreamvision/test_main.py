import sys
import os
import base64
import sqlite3
import pathlib

#local imports
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from dreamvision.dreamvision import save_image, create_image, load_last_image, Dreamvision


def test_save_image():
    if not os.path.exists("./test_images/"):
        os.mkdir("./test_images/")
    image = "iVBORw0KGgoAAAANSUhEUgAAA4QAAAFKCAIAAADKUQaBAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAP+lSURBVHhepP1p32zb"
    image_data = base64.b64decode(image.replace(" ", "+"))
    save_image(image_data, 'test_images', 'test ImAge')
    assert os.path.exists('test_images/test_image.jpg') == True
    save_image(image_data, 'test_images', 'test ImAge')
    assert os.path.exists('test_images/test_image(1).jpg') == True
    os.remove('test_images/test_image.jpg')
    os.remove('test_images/test_image(1).jpg')
    
def test_load_last_image():
    connection = sqlite3.connect('dreams.db')
    cursor = connection.cursor()
    cursor.execute("""insert into dreams (title, description, date, file_name)
        values ('test_image','test image', 2023-01-04, 'test_images/test_image.jpg');""")
    assert load_last_image(connection) == 'test_images/test_image.jpg'
    cursor.execute("""insert into dreams (title, description, date, file_name)
        values ('test_image','test image', 2023-01-04, 'test_images/test_image2.jpg');""")
    assert load_last_image(connection) != 'test_images/test_image.jpg'
    cursor.execute("""delete from dreams where file_name = 'test_images/test_image.jpg'""")

