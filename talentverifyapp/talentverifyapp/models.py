from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=100)
    date_of_registration = models.DateField()
    registration_number = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_person = models.ForeignKey(User, on_delete=models.CASCADE, related_name='companies')
    departments = models.TextField()
    employees_count = models.PositiveIntegerField()
    contact_phone = models.CharField(max_length=20)
    email = models.EmailField()


class Employee(models.Model):
    objects = None
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    date_started = models.DateField()
    date_left = models.DateField(null=True, blank=True)
    duties = models.TextField()
