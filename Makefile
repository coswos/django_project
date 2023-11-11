check:
	ruff check .
	black --check .

fix:
	isort .
	ruff --fix .
	black .


