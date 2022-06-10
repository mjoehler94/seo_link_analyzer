tests:
	- python tests.py

format:
	- black .

update_requirements:
	- pip freeze > requirements.txt

install:
	- pip install -r requirements.txt