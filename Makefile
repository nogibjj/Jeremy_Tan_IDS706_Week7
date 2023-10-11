install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

format:	
	black *.py 

lint:
	ruff check *.py mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	#deploy goes here
		
all: install lint test format deploy

generate_and_push:
	# Create the markdown file 
	python test_main.py 

	# Add, commit, and push the generated files to GitHub
	@if [ -n "$$(git status --porcelain)" ]; then \
		git config --local user.email "action@github.com"; \
		git config --local user.name "GitHub Action"; \
		git add .; \
		git commit -m "Add SQL log"; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi

extract:
	etl-query extract

transform_load: 
	etl-query transform_load

query:
	etl-query general_query "SELECT t1.server, t1.opponent, AVG(t1.seconds_before_next_point) as avg_seconds_before_next_point, COUNT(*) as total_matches_played FROM default.servetimesdb t1 JOIN default.eventtimesdb t2 ON t1.id = t2.id GROUP BY t1.server, t1.opponent ORDER BY total_matches_played DESC LIMIT 10"

setup_package: 
	python setup.py develop --user