from rest_framework import viewsets
from rest_framework.response import Response
from transformations.models import Employee
from .serializers import FirstNameSerializer


def short_view(class_serializer):
    def view(self, request):
        serializer = class_serializer(data=self.request.query_params)
        if serializer.is_valid():
            return Response(serializer.data['result'], status=200)
        return Response(serializer.errors, status=404)
    return view


class EmployeeViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Employee.get_all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        employee = Employee.get_by_pk(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)


class FilterByNameViewSet(viewsets.ViewSet):
    """Viewset filters by first_name"""
    list = short_view(FirstNameSerializer)

