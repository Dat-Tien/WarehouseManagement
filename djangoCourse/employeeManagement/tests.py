from django.test import TestCase
from .models import Employee
from django.urls import reverse
import pytest
import json
import datetime
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.decorators import api_view,  permission_classes
from rest_framework.permissions import IsAuthenticated
from django.urls import path
from . import views

# Create your tests here.
@pytest.mark.django_db
class EmployeeTest(TestCase):
    def empSetup(self):
        Employee.objects.create(job_dept='Consultant', name='Harry', description='This is for testing with Harry', salary_range='1400 USD ~ 2500 USD')
        Employee.objects.create(job_dept='Doctor', name='Koltin', description='Save people life is my destiny', salary_range='5500 USD ~ 7500 USD')


    def empCreate(self):
        emp1 = Employee.objects.get(job_dept='Consultant')
        emp2 = Employee.objects.get(job_dept='Doctor')
        self.assertEqual(emp1, 'The lion says "roar"')
