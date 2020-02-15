# Portfolio Site for Lesley Anne Greene Ceramics

This is the portfolio site for Lesley Anne Greene Ceramics.

This site is build with Django by Jessica Greene 2020.

To get into the virtual enviroment, in the directory use the command `pipenv shell`

From here you can now run the commands for the `Django` site.

This project has two Apps within it (gallery & news) where content can be added through admin.

The postgresql Database requires a password, you can save this in a `.env` file. Copy the `.template_env`, fill in the values and rename it.

Make migrations:

`python manage.py makemigrations`

See migrations as SQL:

`python manage.py sqlmigrate index 0001`

and then to implement them:

`python manage.py migrate`

You can also add the app name at the end to apply migrations only from that app.

Collect Static files:

`python manage.py collectstatic`

Run the server:

`python manage.py runserver`

Run with Gunicorn

`gunicorn portfolio_site.wsgi:application`

Run with Docker via Makefile, first build the image:

`make docker-build`

then run the image:

`make run-in-docker`
