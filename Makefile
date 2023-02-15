setup:
	pip install -e .

install:
	pip install --upgrade pip && pip install -r requirements.txt 

test:
	pytest --ignore=src/dreamvision/test_main.py

lint:
	pylint src

full_test:
	pytest