setup:
	pip install -e .

install:
	pip install --upgrade pip && pip install -r requirements.txt 

test:
	pytest --ignore=src/dreamvision/test_main.py

fulle_test:
	pytest