from rest_framework import viewsets
from rest_framework.response import Response

from es_core.models import Employee
from transformations.models import Employee2
from .transform_filters import transform_filter_names
from es_core.es_helpers.es_filters import (
    match_all
)

from .serializers import EmployeeSerializer, Employee2Serializer


class EmployeeViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Employee2.get_all()
        serializer = Employee2Serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        employee = Employee.es_object.es_get_by_pk(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

