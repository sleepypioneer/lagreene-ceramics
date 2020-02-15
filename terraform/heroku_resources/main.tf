provider "heroku" {
  version = "~> 2.2.1"
}

# terraform {
#   backend "pg" {
#     conn_str = ""
#   }
# }

variable "portfolio_app_name" {
  description = "Name of the Heroku app provisioned as an example"
}

resource "heroku_app" "portfolio_app" {
  name   = "${var.portfolio_app_name}"
  region = "eu"
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
  app = "${heroku_app.portfolio_app.name}"

  source = {
    # A local directory, changing its contents will
    # force a new build during `terraform apply`
    path = "../../app"
  }
}

# Launch the app's web process by scaling-up
resource "heroku_formation" "portfolio_app" {
  app        = "${heroku_app.portfolio_app.name}"
  type       = "web"
  quantity   = 1
  size       = "free"
  depends_on = ["heroku_build.portfolio_app"]
}

# Create a database, and configure the app to use it
resource "heroku_addon" "portfolio_app_database" {
  app  = "${heroku_app.portfolio_app.name}"
  plan = "heroku-postgresql:hobby-dev"
}


output "portfolio_app_url" {
  value = "https://${heroku_app.portfolio_app.name}.herokuapp.com"
}