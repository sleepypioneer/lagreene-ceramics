# Development notes and links for resources

Some notes while developing which may help debug or futuer development work.

```sql
ALTER USER user_name WITH PASSWORD 'new_password';
```

List users:

```psql
 \du
```

```sql
DROP USER name;
```

Make migrations for certain app (in example for `index` app):

```sh
python manage.py makemigrations index
```


deploying

heroku config:set WEB_CONCURRENCY=3
gunicorn hello:app --timeout 10
gunicorn hello:app --max-requests 1200

## Links for depencies documentation

* [Pillow](https://pillow.readthedocs.io/en/latest/installation.html)

## Links for useful tutorials

* [Adding postgres to Django project](https://tutorial-extensions.djangogirls.org/en/optional_postgresql_installation/)
* [Building Django project](https://docs.djangoproject.com/en/3.0/intro/tutorial02/)
* [Deployment Checklist](https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/)
* [Dockerize Django App](https://semaphoreci.com/community/tutorials/dockerizing-a-python-django-web-application)

Invaluable help! https://stackoverflow.com/questions/49742714/collecstatic-does-not-push-to-files-s3
