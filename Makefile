check:
	ruff check .
	black --check .

fix:
	isort .
	ruff --fix .
	black .

run:
	python src/manage.py runserver

mkmig:
	python src/manage.py makemigrations
	python src/manage.py migrate
