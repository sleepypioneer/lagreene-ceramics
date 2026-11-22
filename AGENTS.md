# AGENTS.md

This file provides guidance to AI agents and contributors when working with code in this repository.

## Project Overview

Portfolio website for Lesley Anne Greene Ceramics built with Django 5 and Python 3.11. Deployed to Heroku with PostgreSQL database and optional S3/CloudFront for static/media files.

## Common Commands

```sh
make deps           # Install dependencies (uses uv sync)
make dev            # Run development server on port 8000
make test           # Run all tests (homepage, pages, gallery apps)
make lint           # Lint Python code with pycodestyle
make migrations     # Create new migrations
make migrate        # Apply migrations
make collectstatic  # Collect static files (to S3 if USE_S3=TRUE)
```

Single app test: `uv run python app/manage.py test gallery`

## Environment Setup

1. Copy `app/.template_env` to `app/.env`
2. Required variables:
   - `SECRET_KEY` - Generate with: `uv run python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`
   - `DATABASE_URL` - e.g., `postgres://user@localhost:5432/dbname`
   - `DJANGO_DEBUG=True`
   - `USE_S3=False` (set to TRUE for S3 storage)

## Architecture

All Django code lives in `app/`:

- **lagreeneceramics/** - Project configuration (settings.py, urls.py, storage_backends.py)
- **homepage/** - Homepage with slideshow (`SlideShowItem`) and announcements (`Announcement`)
- **gallery/** - Gallery items with categories and filtering (`GalleryItem`, `Category`)
- **pages/** - Static pages: about, CV, stockists, links (`Link`, `Stockist`, `Venue`)
- **templates/** - Base templates (base.html, navbar.html)
- **static/** - CSS, JS, images

Storage backends in `storage_backends.py` configure S3 locations when `USE_S3=TRUE`.

## Key Patterns

- Database configuration uses `dj-database-url` from `DATABASE_URL` env var
- Static files use WhiteNoise locally, S3 in production
- Custom template tag `static_cdn` in `pages/templatetags/` for CDN URLs
- Admin sorting via `django-admin-sortable2` (`my_order` and `itemOrder` fields)

## Infrastructure

Terraform configuration in `terraform/` deploys to Heroku. See [terraform/README.md](terraform/README.md) for setup instructions.
