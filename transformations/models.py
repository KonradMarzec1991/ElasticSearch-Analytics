from django.db import models
from .transforms import transform_filter_names
from es_core.es_filters import match_all, get_by_id
from .utils import LazyInit


class Employee(LazyInit):
    """
    Representation of serialized model with native Python class
    Inherits from LazyInit class to avoid __init__ usage
    """
    _fields = ['FirstName', 'LastName', 'Address', 'MaritalStatus', 'Gender',
               'Salary', 'Age', 'Interests', 'DateOfJoining', 'Designation']

    @property
    def full_name(self):
        return f'{self.FirstName} {self.LastName}'

    def __str__(self):
        return self.full_name

    @staticmethod
    def get_all():
        return transform_filter_names(match_all())

    @staticmethod
    def get_by_pk(pk):
        return get_by_id(pk)[0]['_source']

