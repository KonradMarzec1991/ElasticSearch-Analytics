from rest_framework import routers
from .views import EmployeeViewSet

employee_router = routers.DefaultRouter()
employee_router.register('employee', EmployeeViewSet, basename='employee')


urlpatterns = [

]
