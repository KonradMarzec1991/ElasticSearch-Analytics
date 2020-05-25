from rest_framework import serializers


class EmployeeSerializer(serializers.Serializer):



    FirstName = serializers.CharField(max_length=100)
    LastName = serializers.CharField(max_length=100)
    Address = serializers.CharField(max_length=100)
    MaritalStatus = serializers.CharField(max_length=100)
    Gender = serializers.CharField(max_length=100)
    Salary = serializers.CharField(max_length=100)
    Age = serializers.IntegerField()
    Interests = serializers.CharField(max_length=100)
    DateOfJoining = serializers.CharField(max_length=100)
    Designation = serializers.CharField(max_length=100)
