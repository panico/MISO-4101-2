web: gunicorn MySmartHome.wsgi --log-file -
web: python manage.py collectstatic --noinput; gunicorn MySmartHome.wsgi
