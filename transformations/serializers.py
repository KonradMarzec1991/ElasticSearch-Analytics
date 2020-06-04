from rest_framework import serializers
from .utils import transform_only

from es_core.es_filters import filter_by_fn


class FirstNameSerializer(serializers.Serializer):
    """
    Serializer for non-model
    """
    first_name = serializers.CharField(max_length=100)
    result = serializers.ReadOnlyField()

    def validate(self, attrs):
        first_name = attrs.get('first_name')
        attrs['result'] = transform_only(
            filter_by_fn(first_name)
        )
        return super().validate(attrs)
