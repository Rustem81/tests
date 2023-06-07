install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv temp\\test_hello.py

format:
	black *.py


lint:
	

	pylint $(find . -name "hello.py" | xargs)

all: install lint test
