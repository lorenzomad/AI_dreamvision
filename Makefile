setup:
	python3 -m venv /.venv

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt &&\
		pip install -e .
test:
	python -m pytest -vv test_*.py

