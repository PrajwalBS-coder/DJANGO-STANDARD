# import os
# from celery import Celery

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_celery.settings")
# app = Celery("django_celery")
# app.config_from_object("django.conf:settings", namespace="CELERY")
# app.autodiscover_tasks()
    # celery.py
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Practice.settings')

app = Celery('Practice', broker=settings.CELERY_BROKER_URL, result_backend=settings.CELERY_RESULT_BACKEND)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)