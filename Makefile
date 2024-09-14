install: 
	pip3 install --upgrade pip && pip3 install -r requirements.txt

format: 
	black *.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

test: 
	python3 -m pytest -cov=main test_main.py

clean:
	rm -rf .pytest_cache

all: install format lint test