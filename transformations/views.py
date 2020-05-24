from rest_framework import viewsets
from rest_framework.response import Response

from .transform_filters import transform_filter_names
from .serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = transform_filter_names('ELVA')
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)
