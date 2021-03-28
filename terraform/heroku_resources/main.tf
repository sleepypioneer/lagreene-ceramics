provider "heroku" {
  version = "~> 2.2.1"
}

terraform {
  backend "pg" {
    conn_str = "postgres://wbeegdkczwjymt:14afcc6e31326f89873f960674c8ff1a6c2508f4c1f6fa97ddbaaf8d2d3489a2@ec2-176-34-97-213.eu-west-1.compute.amazonaws.com:5432/d6lsia9obl2gcr"
  }
}

variable "portfolio_app_name" {
  description = "Name of the Heroku app provisioned as an example"
}

resource "heroku_app" "portfolio_app" {
  name   = "var.portfolio_app_name"
  region = "eu"
  acm = true
}

resource "heroku_config" "portfolio_app" {
    vars = {
      DJANGO_DEBUG = "False"
    }

    sensitive_vars = {
        SECRET_KEY = "u7%v56nt7kflofaci1z%qwyt81)9hkvwi0oy2_xgk^uli8ulh0"
    }
}

# Build code & release to the app
resource "heroku_build" "portfolio_app" {
  app = "heroku_app.portfolio_app.name}"

  source = {
    # A local directory, changing its contents will
    # force a new build during `terraform apply`
    path = "../../app"
  }
}

# Launch the app's web process by scaling-up
resource "heroku_formation" "portfolio_app" {
  app        = "heroku_app.portfolio_app.name}"
  type       = "web"
  quantity   = 1
  size       = "hobby"
  depends_on = [heroku_build.portfolio_app]
}

# Create a database, and configure the app to use it
resource "heroku_addon" "portfolio_app_database" {
  app  = "heroku_app.portfolio_app.name}"
  plan = "heroku-postgresql:hobby-dev"
}


output "portfolio_app_url" {
  value = "https://${heroku_app.portfolio_app.name}.herokuapp.com"
}