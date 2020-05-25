from rest_framework import serializers


class EmployeeSerializer(serializers.Serializer):

    gender_options = (
        ('Female', 'Female'),
        ('Male', 'Male')
    )

    martial_choices = (
        ('Married', 'Married'),
        ('Unmarried', 'Unmarried')
    )

    FirstName = serializers.CharField(max_length=100)
    LastName = serializers.CharField(max_length=100)
    Address = serializers.CharField(max_length=100)
    MaritalStatus = serializers.ChoiceField(choices=martial_choices)
    Gender = serializers.ChoiceField(choices=gender_options)
    Salary = serializers.IntegerField()
    Age = serializers.IntegerField()
    Interests = serializers.CharField(max_length=100)
    DateOfJoining = serializers.DateField()
    Designation = serializers.CharField(max_length=100)

    def validate_Age(self, value):
        if value < 0:
            raise ValueError('Must be grater than 0')
        return value
