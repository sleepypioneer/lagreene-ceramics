FROM python:3.11-buster

RUN apt update && apt install -y gcc libc-dev libffi-dev

# WORKDIR sets the working directory for docker instructions
WORKDIR /app

ARG SECRET_KEY
ARG DATABASE_NAME
ARG DATABASE_USER
ARG DATABASE_URL
ARG DATABASE_PASSWORD
ARG DATABASE_HOST
ARG DATABASE_PORT
ARG DJANGO_DEBUG
ARG 'dev'

ENV SECRET_KEY=$SECRET_KEY
ENV DATABASE_NAME=$DATABASE_NAME
ENV DATABASE_USER=$DATABASE_USER
ENV DATABASE_URL=$DATABASE_URL
ENV DATABASE_PASSWORD=$DATABASE_PASSWORD
ENV DATABASE_HOST=$DATABASE_HOST
ENV DATABASE_PORT=$DATABASE_PORT
ENV DJANGO_DEBUG=$DJANGO_DEBUG

EXPOSE 8000

# Install other requirements
COPY app/requirements.txt .
RUN pip install -r requirements.txt

# Copy application code.
COPY app/. .

# Create a group and user to run our app
ARG APP_USER=appuser
RUN groupadd -r $APP_USER && useradd --no-log-init -r -g $APP_USER $APP_USER

# Install assets
RUN python manage.py collectstatic --noinput --clear

# Run application
STOPSIGNAL SIGINT
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]