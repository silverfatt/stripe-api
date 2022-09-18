VENV ?= .venv
CODE = tests app



.PHONY: admin
up:
	python manage.py createsuperuser

.PHONY: up
up:
	python manage.py runserver 0.0.0.0:80

