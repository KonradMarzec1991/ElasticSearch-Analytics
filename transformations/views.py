# pylint: disable=no-self-use,unused-argument,abstract-class-instantiated
"""
ElasticSearch Viewsets
"""

from django.http import HttpResponse

try:
    from io import BytesIO as IO
except ImportError:
    from io import StringIO as IO

import pandas as pd
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from es_core.es_filters import filter_by_age
from .es_to_excel import normalize_es_output
from .serializers import FirstNameSerializer, GeneralFilterSerializer

EXCEL_TYPE = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'


def short_view(class_serializer):
    """Short_view function overrides list method with serializer class"""
    def view(self, request):
        """View function"""
        serializer = class_serializer(data=self.request.query_params)
        if serializer.is_valid():
            return Response(serializer.validated_data['result'], status=200)
        return Response(serializer.errors, status=404)
    return view


class FilterByNameViewSet(viewsets.ViewSet):
    """Viewset filters by first_name"""
    list = short_view(FirstNameSerializer)

    @action(detail=False)
    def export_to_excel(self, request):
        """Action exporting to Excel file retireve from ElasticSearch"""
        es_retrieve = filter_by_age(50)
        df = normalize_es_output(es_retrieve)

        io_file = IO()
        excel_file = pd.ExcelWriter(io_file, engine='xlsxwriter')
        df.to_excel(excel_file, sheet_name='es_stats')

        excel_file.save()
        excel_file.close()
        io_file.seek(0)

        response = HttpResponse(excel_file.read(), content_type=EXCEL_TYPE)
        response['Content-Disposition'] = 'attachment; filename=stats.xlsx'
        return response


class GeneralFilterViewSet(viewsets.ViewSet):
    """Viewset filters by (multiple) employee attrs"""
    list = short_view(GeneralFilterSerializer)
