# Development notes and links for resources 🗒️

Some notes taken while developing which may help debug or futuer development work.

## Useful Commands ⌨️

### SQL

```sql
ALTER USER user_name WITH PASSWORD 'new_password';

DROP USER name;
```

### PSQL

List users:

```psql
 \du
```

Make migrations for certain app (in example for `index` app):

```sh
python manage.py makemigrations index
```

### When Deploying to Heroku 🌐

heroku config:set WEB_CONCURRENCY=3
gunicorn hello:app --timeout 10
gunicorn hello:app --max-requests 1200


## Useful Links 🔗

### Depencies documentation 📖

* [Pillow](https://pillow.readthedocs.io/en/latest/installation.html)


### Revelant Tutorials 👩‍🎓

* [Adding postgres to Django project](https://tutorial-extensions.djangogirls.org/en/optional_postgresql_installation/)
* [Building Django project](https://docs.djangoproject.com/en/3.0/intro/tutorial02/)
* [Deployment Checklist](https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/)
* [Dockerize Django App](https://semaphoreci.com/community/tutorials/dockerizing-a-python-django-web-application)
* [Postgres 12 for Ubuntu 19](https://www.osradar.com/how-to-install-postgresql-on-ubuntu-19-04/)
* [Local copy of postgres database](https://medium.com/@johngrant/django-and-heroku-postgres-databases-6c22ffd71081)

💰 Invaluable help! https://stackoverflow.com/questions/49742714/collecstatic-does-not-push-to-files-s3
