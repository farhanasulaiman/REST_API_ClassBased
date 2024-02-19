from rest_framework import serializers

from RESTAPI_ClassBasedApp.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('emp_id', 'emp_name', 'salary')
