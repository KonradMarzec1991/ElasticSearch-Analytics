from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from transformations.views import GeneralFilterViewSet, FilterByNameViewSet

employee_router = routers.DefaultRouter()
employee_router.register(
    'general',
    GeneralFilterViewSet,
    basename='general'
)
employee_router.register(
    'filter_by_name',
    FilterByNameViewSet,
    basename='filter_by_name'
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(employee_router.urls))
]
