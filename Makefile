.PHONY: docker-build run-in-docker createsuperuser

DOCKER_BUILD_CONTEXT='./'
DOCKER_NAME='lagreeneceramics'
DOCKER_TAG='alpha'

docker-build:
	docker build \
		-f $(DOCKER_BUILD_CONTEXT)/Dockerfile \
		--build-arg  SECRET_KEY='${SECRET_KEY}' \
		--build-arg  DATABASE_NAME='${DATABASE_NAME}' \
		--build-arg  DATABASE_USER='${DATABASE_USER}' \
		--build-arg  DATABASE_URL='${DATABASE_URL}' \
		--build-arg  DATABASE_PASSWORD='${DATABASE_PASSWORD}' \
		--build-arg  DATABASE_HOST='${DATABASE_HOST}' \
		--build-arg  DATABASE_PORT='${DATABASE_PORT}' \
		--build-arg  DJANGO_DEBUG='${DJANGO_DEBUG}' \
		-t $(DOCKER_NAME):$(DOCKER_TAG) \
		$(DOCKER_BUILD_CONTEXT)

run-in-docker:
	docker run --rm \
	-p 8000:8000 \
	--name $(DOCKER_NAME) \
	$(DOCKER_NAME):$(DOCKER_TAG)

docker-clean:
	docker rm -f $(DOCKER_NAME) || true
	docker image rm $(DOCKER_NAME):$(DOCKER_TAG) || true

create-super-user:
	docker exec -it $(DOCKER_NAME) python manage.py createsuperuser


.PHONY: deps migrations migrate collectstatic dev
deps:
	poetry install

migrations:
	poetry run python app/manage.py makemigrations

migrate:
	poetry run python app/manage.py migrate

collectstatic:
	poetry run python app/manage.py collectstatic

dev:
	poetry run python app/manage.py runserver

create-requirements-file: 
	poetry export --format requirements.txt --without-hashes -o requirements.txt
	poetry export --format requirements.txt --without-hashes -o app/requirements.txt