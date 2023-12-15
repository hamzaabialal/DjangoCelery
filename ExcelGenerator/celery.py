from celery import Celery
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ExcelGenerator.settings')
app = Celery('ExcelGenerator', broker='redis://localhost:6379/0')

# Configuration from Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover tasks in all registered apps
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Requests: {self.request!r}")
