from rest_framework import serializers
from .utils import transform_only

from es_core.es_filters import filter_by_fn


class EmployeeSerializer(serializers.Serializer):
    """
    Simple serializer for `Employee` class
    """

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


class Employee2Serializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    result = serializers.ReadOnlyField()

    def validate(self, attrs):
        first_name = attrs.get('first_name')
        attrs['result'] = transform_only(
            filter_by_fn(first_name)
        )
        return super().validate(attrs)

    class Meta:
        fields = ('result', )