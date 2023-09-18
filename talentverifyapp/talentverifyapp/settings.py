import os
from django.db import models
import django.contrib.auth.models


class Company(models.Model):
    name = models.CharField(max_length=100)
    date_of_registration = models.DateField()
    registration_number = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_person = models.ForeignKey(django.contrib.auth.models.User,
                                       on_delete=models.CASCADE, related_name='companies')
    departments = models.TextField()
    employees_count = models.PositiveIntegerField()
    contact_phone = models.CharField(max_length=20)
    email = models.EmailField()


class Employee(models.Model):
    objects = None
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


# ...

# Add the path to your React app
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DIRS = [
    os.path.join(BASE_DIR, 'talent-verify-app/build'),
]

# ...

# Configure static files to be served by Django
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'talent-verify-app/build/static'),
]
