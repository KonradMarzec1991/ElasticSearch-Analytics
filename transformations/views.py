from rest_framework import viewsets
from rest_framework.response import Response

from .transform_filters import transform_filter_names
from es_core.es_helpers.es_filters import filter_by_fn
from .serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = transform_filter_names(filter_by_fn('ELVA'))
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)
