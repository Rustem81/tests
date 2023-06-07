install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv temp\test_hello.py

format:
	black *.py


lint:
	pylint --disable=R,C temp\hello.py

all: install lint test
