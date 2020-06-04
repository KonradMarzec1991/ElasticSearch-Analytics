from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import FirstNameSerializer, GeneralFilterSerializer


def short_view(class_serializer):
    def view(self, request):
        serializer = class_serializer(data=self.request.query_params)
        if serializer.is_valid():
            return Response(serializer.data['result'], status=200)
        return Response(serializer.errors, status=404)
    return view


class FilterByNameViewSet(viewsets.ViewSet):
    """Viewset filters by first_name"""
    list = short_view(FirstNameSerializer)


class GeneralFilterViewSet(viewsets.ViewSet):
    """Viewset filters by (multiple) employee attrs"""
    list = short_view(GeneralFilterSerializer)

