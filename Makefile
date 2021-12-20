install:
	pip install -e .['dev']

test:
	FLASK_ENV=test pytest tests/ -v --cov=sitegu

run:
	FLASK_APP=sitegu/app.py FLASK_ENV=development flask run