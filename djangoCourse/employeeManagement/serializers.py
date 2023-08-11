from rest_framework import serializers
from models import Employee, JobDepartment, Leave, Payroll, Qualification, SalaryOrBonus


class EmployeeSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data['fname'] == data['lname']:
            raise serializers.ValidationError("fname and lname shouldn't be same.")
        return data
    
    class meta:
        model = Employee
        fields = ['emp_ID', 'fname', 'lname', 'gender', 'age', 'contact_add', 'emp_email', 'emp_pass']

class JobDepartmentSerializer(serializers.ModelSerializer):
    class meta:
        model = JobDepartment
        fields = ['job_ID', 'job_dept', 'name', 'description', 'salary_range']

class LeaveSerializer(serializers.ModelSerializer):
    emp_ID = EmployeeSerializer(read_only=True)
    class meta:
        model = Leave
        fields = ['leave_ID', 'emp_ID', 'date', 'reason']

class SalaryOrBonusSerializer(serializers.ModelSerializer):
    job_ID = JobDepartmentSerializer(read_only=True)
    class meta:
        model = SalaryOrBonus
        fields = ['salary_ID', 'job_ID', 'amount', 'anual', 'bonus']

class PayrollSerializer(serializers.ModelSerializer):
    emp_ID = EmployeeSerializer(read_only=True)
    job_ID = JobDepartmentSerializer(read_only=True)
    salary_ID = SalaryOrBonusSerializer(read_only=True)
    leave_ID = LeaveSerializer(read_only=True)
    class meta:
        model = Payroll
        fields = ['enroll_ID', 'emp_ID', 'job_ID', 'salary_ID', 'leave_ID', 'date', 'report', 'total_amount']

class QualificationSerializer(serializers.ModelSerializer):
    emp_ID = EmployeeSerializer(read_only=True)
    class meta:
        model = Qualification
        fields = ['qual_ID', 'emp_ID', 'position', 'requirements', 'date_in']