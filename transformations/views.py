from rest_framework import viewsets
from rest_framework.response import Response
from transformations.models import Employee
from .serializers import EmployeeSerializer, Employee2Serializer


class EmployeeViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Employee.get_all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        employee = Employee.get_by_pk(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)


class FilterByNameViewSet(viewsets.ReadOnlyModelViewSet):

    def list(self, request):
        serializer = Employee2Serializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data, status=200)

