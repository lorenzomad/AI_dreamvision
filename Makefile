setup:
	pip install -e .

install:
	pip install --upgrade pip && pip install -r requirements.txt 

test:
	python -m pytest --ignore src/dreamvision/test_dreamvision.py

lint:
	pylint --disable=C src

full_test:
	python -m pytest