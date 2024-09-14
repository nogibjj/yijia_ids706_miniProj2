install: 
	pip3 install --upgrade pip && pip3 install -r requirements.txt

format: 
	black *.py

lint:
	flake8 --ignore=E501 *.py

test: 
	python3 -m pytest -cov=main test_main.py

clean:
	rm -rf .pytest_cache

generate_profile_report:
	python -c "from main import load_data, generate_profile_report; \
	data = load_data('rdu-weather-history.csv'); \
	generate_profile_report(data, 'profile_report.html', 'profile_report.md')"

   # Git commands to add, commit, and push the report
	@if [ -n "$$(git status --porcelain)" ]; then \
	    git config --local user.email "action@github.com"; \
	    git config --local user.name "GitHub Action"; \
	    git add profile_report.md; \
	    git commit -m 'Add generated markdown report'; \
	    git push; \
	else \
	    echo "No changes to commit."; \
	fi

all: install format lint test generate_profile_report
