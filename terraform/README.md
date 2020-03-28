# Heroku & Terraform infrastructure

## Setup

After running `pipenv install` and `pipenv shell` `cd` into the `heroku_resources` directory and run `terraform init`.
Next run the command below and when prompted enter the name for your app ie `lagreeneceramics`.

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

and create the file t`current.tfplan` in the current directory. To apply these changes run:

```sh
terraform apply "current.tfplan"
```

This will error as it will be unable to complete the process, you will first need to set up the `$DATABASE_URL`. To do so run the following commands:

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

You should also now copy the `DATABASE_URL` to the `.env` file in the root directory.

We will also stop the app from collecting its static files at the moment by running: `heroku config:set DISABLE_COLLECTSTATIC=1 --app $APP_NAME`

You now can run `terraform init` again, be sure to use the same value for the `APP NAME` when prompted about copying the existing state respond `yes`. You can now rerun `terraform plan -out=current.tfplan` (again giving the same APP NAME) and finally to apply the changes `terraform apply "current.tfplan"`.

We will need to get the database credentials via the resources tab in the heroku dashboard for the app, then click on settings and credentials in the datastores view. From there you can copy the values for host, database name, user, and password into the `.env` file and also set them as config variables for your heroku app with the following command:

```sh
heroku config:set <CONFIG-NAME>=<CONFIG-VALUE> --app $APP_NAME
```

You will also want to add the secret key and django debug config to heroku, though the debug will now be set to false for the production environment.
