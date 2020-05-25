from rest_framework import serializers
from es_core.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class Employee2Serializer(serializers.Serializer):
    FirstName = serializers.CharField(max_length=100)
    LastName = serializers.CharField(max_length=100)
    Address = serializers.CharField(max_length=100)
    MaritalStatus = serializers.CharField(max_length=100)
    Gender = serializers.CharField(max_length=100)
    Salary = serializers.CharField(max_length=100)
    Age = serializers.CharField(max_length=100)
    Interests = serializers.CharField(max_length=100)
    DateOfJoining = serializers.CharField(max_length=100)
    Designation = serializers.CharField(max_length=100)
