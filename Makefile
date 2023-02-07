setup:
	pip install -e .

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt 

test:
	export PYTHONPATH=. &&\
		python -m pytest

