# Portfolio Site for Lesley Anne Greene Ceramics <img src="docs/images/PottersMark_cyan.png" width="30" alt-text="potters mark of Lesley Anne Greene">

This is the portfolio site for Lesley Anne Greene a ceramics artists based in North Yorkshire, United Kingdom.


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

There is a pipenv virtual environment set up for this repo. To install all the packages and enter it's shell use the following commands:

``` sh 
# in the root directory
pipenv install
pipenv shell
```

ℹ️ If you want to create an app and resources from this code you can do so with terraform, more information on how to do so can be found [here](../terraform/READMe.md)

The postgresql Database requires a password, you can save this in a `.env` file. Copy the `.template_env`, fill in the values and rename it.

To run the following Django commands you must be inside the pipenv shell and `cd` into the `/app` directory:

``` sh
# Make migrations
python manage.py makemigrations

# See migrations as SQL:
python manage.py sqlmigrate index 0001

# Implement migrations
python manage.py migrate

# You can also add the app name at the end to apply migrations only from that app.

#Collect Static files
python manage.py collectstatic

#Run the server default port is 8000
python manage.py runserver
```

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