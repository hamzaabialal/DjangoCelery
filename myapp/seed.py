from .models import *
from faker import Faker
fake = Faker()

import random
def seed_db(n):
    for i in range(0, n):
        Student.objects.create(
        student_name = fake.name(), 
        student_age = random.randint(0,50)
        )