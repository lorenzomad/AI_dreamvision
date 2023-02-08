setup:
	pip install -e .

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt 

test:
	PYTHONPATH=. pytest

