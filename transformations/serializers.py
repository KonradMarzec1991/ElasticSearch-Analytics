"""
Serializes handle non-model objects
"""


from rest_framework import serializers
from .utils import transform_only, add_to_kwargs

from es_core.es_filters import filter_by_fn, general_filter


class FirstNameSerializer(serializers.Serializer):
    """FirstNameSerializer validates first_name and retrieves ES data"""
    first_name = serializers.CharField(max_length=100)
    result = serializers.ReadOnlyField()

    def validate(self, attrs):
        first_name = attrs.get('first_name')
        attrs['result'] = transform_only(
            filter_by_fn(first_name)
        )
        return super().validate(attrs)


class GeneralFilterSerializer(serializers.Serializer):
    """GeneralFilterSerialzer allows to filter by employee attrs"""
    first_name = serializers.CharField(max_length=100, default=None)
    last_name = serializers.CharField(max_length=100, default=None)
    age = serializers.IntegerField(default=None)
    gender = serializers.CharField(max_length=10, default=None)
    interests = serializers.CharField(max_length=100, default=None)
    martial_status = serializers.CharField(max_length=15, default=None)
    designation = serializers.CharField(max_length=50, default=None)

    def validate(self, attrs):
        """Main validation method - adds result attr"""
        attrs['result'] = transform_only(
            general_filter(**add_to_kwargs(attrs))
        )
        return super().validate(attrs)

    def validate_age(self, age):
        """Validates if age is zero or less"""
        if age is not None and age <= 0:
            raise serializers.ValidationError('Age must greater than 0')
        return age

    def validate_gender(self, gender):
        """Validates if gender is proper word"""
        if gender is not None and gender not in ('Female', 'Male'):
            raise serializers.ValidationError('Gender must be female or male')
        return gender

    def validate_martial_status(self, status):
        """Validates status of employee"""
        if status is not None and status not in ('Unmarried', 'Married'):
            raise serializers.ValidationError('Unmarried or Married allowed')
        return status


