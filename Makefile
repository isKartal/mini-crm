build:
	docker-compose up --build

up:
	docker-compose up

down:
	docker-compose down

migrate:
	docker-compose run --rm web python manage.py migrate

createsuperuser:
	docker-compose run --rm web python manage.py createsuperuser

seed:
	docker-compose run --rm web python manage.py populate_data 50

shell:
	docker-compose run --rm web python manage.py shell

setup: migrate seed
	@echo "Setup complete! Don't forget to create a superuser with 'make createsuperuser' if needed."
