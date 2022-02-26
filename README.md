# Portfolio Site for Lesley Anne Greene Ceramics <img src="docs/images/PottersMark_cyan.png" width="30" alt-text="potters mark of Lesley Anne Greene">

This is the portfolio site for Lesley Anne Greene a ceramic artists based in East Yorkshire, in the United Kingdom.


## Development 🐍🖥️

This project uses the following technologies

* Python 3.8
* Django 3
* pytest
* Javascript, Jquery
* HTML & CSS
* Bootstrap 4
* Terraform
* It is connected to a postgresql database instance
* Static files are saved to Amazon S3


### Getting started ⚙️

#### Virtual environment

This project uses poetry for package management for local development. To install dependencies run (from root):

``` sh 
make deps
```

##### Setting environment variables

The postgresql Database requires a password, you can save this in a `.env` file. Copy the `.template_env`, fill in the values and rename it.

#### Running the App locally

``` sh
# Make migrations
make migrations

# Implement migrations
make migrate

# You can also add the app name at the end to apply migrations only from that app.

#Collect Static files - if $USE_S3 is set to TRUE then files will be saved to S3 Bucket
make collectstatic

#Run the server default port is 8000
make dev
```

#### Creating a local database for local development

For development you may want to have your own local database and save static files locally instead of using Amazon S3.

A local copy of the Heroku postgres can be made with the following command:

``` sh
PGUSER=postgres PGPASSWORD=password heroku pg:pull DATABASE_URL nameforlocaldb --app lagreene-ceramics
```

*Note that PGUSER and PGPASSWORD set the authentication credentials for the local db, and the Django app has the database URL saved as an environment variable.*

*If the above doesn't work it may be necessary

[DJ-Database-URL](https://github.com/kennethreitz/dj-database-url) utility is used to configure the enbironment variable of the database so all that is now needed is to update the `$DATABASE_URL` value to the new local database:

``` sh
DATABASE_URL=postgres://postgres:password@localhost:5432/nameforlocaldb
```
You will have to run the migrations on the local database and also create a super user `python3 manage.py createsuperuser`.


To stop using S3 for static and media files set the environment variable `$USE_S3` to `FALSE`.

#### Creating infrastructure with Terraform

ℹ️ If you want to create an app and resources from this code you can do so with terraform, more information on how to do so can be found [here](../terraform/READMe.md)

#### Starting the app with Gunicorn 🦄

You can also run the App with Gunicorn by running  `gunicorn portfolio_site.wsgi:application`


#### Run inside a container with Docker 🐋

The app can also be ran within a docker container, first build the app with:

`make docker-build`

then run the image:

`make run-in-docker`

#### Other documentation 🗒️

[Here](docs/development_notes.md) you will find some notes taken during the development of this site which include useful commands, links and tutorials.


### Linting 🚩

This project has python linting set up using [pycodestyle]() to run it use `pycodestyle .` [Autopep 8]() can be used to change files in place with the following command: `autopep8 --in-place --aggressive --aggressive ./<file-path>`


### Core Styles 🎨

For reference here are the main colours and font styling, for more information please look in the relevant CSS file.

``` css
Headings and navbar:            #88A0A8
Paragraph/ text:                #66666E
Background:                     #EFEEEA
Contrast background:            #EEE3AB

Fonts:
Main:                          Archivo Narrow

```

### Feedback Welcome! 📨

See something which could be improved? Please feel free to open a pull request, open an issue or message [@sleepypioneer](https://github.com/sleepypioneer) :)