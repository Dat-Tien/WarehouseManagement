from django.db import models

# Create your models here.

class Employee(models.Model):
    fname = models.CharField(max_length=255, null=False)
    lname = models.CharField(max_length=255, null=False)
    gender = models.IntegerField()
    age = models.IntegerField()
    contact_add = models.CharField(max_length=255)
    emp_email = models.CharField(max_length=255)
    emp_pass = models.CharField(max_length=255)

    def __str__(self):
        return "Employee: " + self.fname + " " + \
                self.lname

class JobDepartment(models.Model):
    job_dept = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    salary_range = models.CharField(max_length=50)

    def __str__(self):
        return "Department " + self.job_dept + " name: " +\
                self.name + " salary range: " + self.salary_range
    
class SalaryOrBonus(models.Model):
    job_ID = models.ForeignKey(JobDepartment, on_delete=models.CASCADE)
    amount = models.IntegerField()
    annual = models.DateField()
    bonus = models.DateField()

    def __str__(self):
        return "Salary: " + self.amount

class Leave(models.Model):
    emp_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    reason = models.TextField()

    def __str__(self):
        return "Leave reason: " + self.reason
      
class Payroll(models.Model):
    emp_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job_ID = models.ForeignKey(JobDepartment, on_delete=models.CASCADE)
    salary_ID = models.ForeignKey(SalaryOrBonus, on_delete=models.CASCADE)
    leave_ID = models.ForeignKey(Leave, on_delete=models.CASCADE)
    date = models.DateField()
    report = models.TextField()
    total_amount = models.IntegerField()

    def __str__(self):
        return "Total payroll: " + self.total_amount
    
class Qualification(models.Model):
    emp_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    position = models.CharField(max_length=30)
    requirements = models.CharField(max_length=30)
    date_in = models.DateField()

    def __str__(self):
        return "Position: " + self.position + " " +\
                " with requirents: " + self.requirements
