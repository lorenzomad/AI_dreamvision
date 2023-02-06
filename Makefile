setup:
	python3 -m venv /.venv

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt 

setup:
	python setup.py develop
		
test:
	cd app/ &&\
	export PYTHONPATH=. &&\
	python -m pytest &&\
	cd ../

