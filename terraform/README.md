# Heroku & Terraform infrastructure 🔩

## Setup

### 1. Initilise the workspace

After running `pipenv install` and `pipenv shell` `cd` into the `heroku_resources` directory and run `terraform init`.

### 2. Create inital plan

Next run the command below and when prompted enter the name for your app ie `lagreene-ceramics`.

```sh
terraform plan -out=current.tfplan
```

This will produce an output similar to the one below:

```sh
Terraform will perform the following actions:

  # heroku_addon.portfolio_app_database will be created
  + resource "heroku_addon" "portfolio_app_database" {
      + app         = "lagreeneceramics"
      + config_vars = (known after apply)
      + id          = (known after apply)
      + name        = (known after apply)
      + plan        = "heroku-postgresql:hobby-dev"
      + provider_id = (known after apply)
    }

  # heroku_app.portfolio_app will be created
  + resource "heroku_app" "portfolio_app" {
      + all_config_vars       = (sensitive value)
      + config_vars           = (known after apply)
      + git_url               = (known after apply)
      + heroku_hostname       = (known after apply)
      + id                    = (known after apply)
      + internal_routing      = (known after apply)
      + name                  = "lagreeneceramics"
      + region                = "eu"
      + sensitive_config_vars = (sensitive value)
      + stack                 = (known after apply)
      + uuid                  = (known after apply)
      + web_url               = (known after apply)
    }

  # heroku_build.portfolio_app will be created
  + resource "heroku_build" "portfolio_app" {
      + app               = "lagreeneceramics"
      + buildpacks        = (known after apply)
      + id                = (known after apply)
      + local_checksum    = "SHA256:7a25da8dcad7f8a3d3eb2261ada649eb9212973e82dbbf20922d75ca4a762185"
      + output_stream_url = (known after apply)
      + release_id        = (known after apply)
      + slug_id           = (known after apply)
      + source            = {
          + "path" = "../../app"
        }
      + stack             = (known after apply)
      + status            = (known after apply)
      + user              = (known after apply)
      + uuid              = (known after apply)
    }

  # heroku_config.portfolio_app will be created
  + resource "heroku_config" "portfolio_app" {
      + id             = (known after apply)
      + sensitive_vars = (sensitive value)
      + vars           = {
          + "DJANGO_DEBUG" = "False"
        }
    }

  # heroku_formation.portfolio_app will be created
  + resource "heroku_formation" "portfolio_app" {
      + app      = "lagreeneceramics"
      + id       = (known after apply)
      + quantity = 1
      + size     = "Free"
      + type     = "web"
    }

Plan: 5 to add, 0 to change, 0 to destroy.
```

and create the file `current.tfplan` in the current directory. To apply these changes run:

```sh
terraform apply "current.tfplan"
```

---

### 3. Set the Database URL

The above will error as it will be unable to complete the process, you will first need to set up the `$DATABASE_URL`. To do so run the following commands:

```sh
export APP_NAME=<YOUR-APP-NAME>
export DATABASE_URL=`heroku config:get DATABASE_URL --app $APP_NAME`
echo $DATABASE_URL # return the database url so you can copy it
```

Copy from the terminal the database url and copy it in to the `main.tf` file in the commented out code, then uncomment this code (it should look like below)

```sh
terraform {
  backend "pg" {
    conn_str = <DATABASE-URL>
  }
}
```

You should also now copy the `DATABASE_URL` to the `.env` file in the root directory ~(see section below)

You now can run `terraform init` again to reinitialise the workspace with the new backend, be sure to use the same value for the `APP NAME` when prompted about copying the existing state respond `yes`.

---


### 4. Add config variables to Heroku

We will also need to update the rest of our config variables both in Heroku and locally. We can retrieve the database credentials via the resources tab in the heroku dashboard for the app, then click on settings and credentials in the datastores view. From there you can copy the values for host, database name, user, and password into the `.env` file and also set them as config variables for your heroku app with the following command:

```sh
heroku config:set <CONFIG-NAME>=<CONFIG-VALUE> --app $APP_NAME
```

You will also want to add the rest of the local environment variables (inside the .env file) including secret key, django debug and aws details to heroku. Note the debug will now be set to false for the production environment. 

You can enter the console of the app in Heroku to make sure the migrations have run and create an admin user with the command `python manage.py createsuperuser`.

Then rerun `terraform plan -out=current.tfplan` (again giving the same APP NAME) and finally to apply the changes `terraform apply "current.tfplan"`.

---

### Updating Code

Now each time the code is updated you can run:

```sh
terraform plan -out=current.tfplan # enter App Name
# and then
terraform apply "current.tfplan"
```

This will deploy the changes in the app to heroku. 

#### Addning new requirement

If you have added new packages do not forget to update the `requirements.txt` there is a make target to do this inside `./app` (you will still have to remove `pkg-resources==0.0.0` manually after running this command)

#### Adding a super user **Important for the first time**

The first time you may have to run some of the `python manage.py` commands in the console of your Heroku app including creating a super user to be able to access the admin panel. `python manage.py createsuperuser`
