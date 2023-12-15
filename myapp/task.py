from celery import shared_task
import time
import pandas as pd
from .models import *
import uuid

def handle_sleep():
    print("Handle SLeep Started!")
    time.sleep(20)

from django.conf import settings
@shared_task
def export_student_excel():
    objs = Student.objects.all()
    payload = []
    for obj in objs:
        payload.append({
            "name": obj.student_name,
            "age": obj.student_age 
        })
    df = pd.DataFrame(payload)
    df.to_csv(f"{uuid.uuid4()}.csv", encoding="UTF-8")    