from django.db import models
from django.conf import settings
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
# Create your models here.

class Worker(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    ENGINEER = 'Engineer'
    WORKER = 'Worker'
    SUPERVISER = 'Superviser'
    CONSULTANT = 'Consultant'
    OCCUPATION_CHOICES = [
        (ENGINEER, 'Engineer'),
        (WORKER, 'Worker'),
        (SUPERVISER, 'Superviser'),
        (CONSULTANT, 'Consultant')
    ]
    occupation = models.CharField(null=False, max_length=20, choices=OCCUPATION_CHOICES, default='Worker')
    full_time = models.BooleanField(default=False)   
    image = models.ImageField(upload_to='images/')
    account = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    mobilePhone = models.CharField(max_length=11)
    workEmail = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username
    
class BasicInfo(models.Model):
    workerId = models.OneToOneField(Worker, on_delete=models.CASCADE)
    dateOfBirth = models.DateField()
    gender = models.CharField(max_length=20)
    maritalStatus = models.CharField(max_length=7)
    nationality = models.CharField(max_length=50)
    Ethnic = models.CharField(max_length=20)
    bankAccount = models.CharField(max_length=50)

    def isValidDateOfBirth(self):
        now = date.today()
        return (
            (now.year - self.dateOfBirth.year < 18) or (
            (now.year - self.dateOfBirth.year == 18) and (
            (now.month < self.dateOfBirth.month) or (
            (now.month - self.dateOfBirth.month == 0) and (now.day < self.dateOfBirth.day))
            )))

    def __str__(self):
        return "Basic info: " + str(self.dateOfBirth) + " " + self.gender

class ContactInfo(models.Model):
    workerId = models.OneToOneField(Worker, on_delete=models.CASCADE)
    homePhone = models.CharField(max_length=20)
    personalEmail = models.CharField(max_length=100)
    permanentAddress = models.CharField(max_length=200)
    nationalInfo = models.CharField(max_length=20, default="", null=False)
    dateOfIssue = models.DateField()
    placeOfIssue = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.workerId + " " + self.homePhone
    
class EmerContactInfo(models.Model):
    workerId = models.ForeignKey(Worker, on_delete=models.CASCADE)
    phoneNumber=models.CharField(max_length=12)
    SIBLINGS = 'Siblings'
    PARENTS = 'Parents'
    RELATIVE = 'Relative'
    RELATIONSHIP = [
        (SIBLINGS, 'Siblings'),
        (PARENTS, 'Parents'),
        (RELATIVE, 'Relative')
    ]
    relationship=models.CharField(max_length=50, choices=RELATIONSHIP, default="", null=False)

    def __str__(self):
        return "Emer contact info: " + self.phoneNumber + " " +\
                self.relationship
