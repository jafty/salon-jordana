# Salon Jordana

Django city guide/blog project for afro hair salons and boutiques in Toulouse.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Railway deployment

1. Push this repository to GitHub.
2. Create a Railway project and link the repository.
3. Add a PostgreSQL service.
4. Set environment variables (see `.env.example`).
5. Deploy. `railway.json` runs migrations + collectstatic + gunicorn.
6. Validate health endpoint: `/healthz/`.

## Required environment variables

- `SECRET_KEY`
- `DEBUG=False`
- `ALLOWED_HOSTS` (comma-separated, include your Railway hostname)
- `CSRF_TRUSTED_ORIGINS` (comma-separated HTTPS origins)
- `DATABASE_URL` (provided by Railway PostgreSQL)

## Static files

WhiteNoise is configured for static assets in production.

## Notes

- Media uploads are currently local (`/media`). For persistent production uploads, use object storage (e.g. S3/Cloudinary).
