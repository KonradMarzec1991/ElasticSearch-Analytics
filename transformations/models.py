# pylint: disable=no-member, cyclic-import
"""
Employee model coresponding to ElasticSearch structure
"""

from es_core.es_filters import match_all, get_by_id
from .utils import LazyInit, transform_filter_names


class Employee(LazyInit):
    """
    Representation of serialized model with native Python class
    Inherits from LazyInit class to avoid __init__ usage
    """
    _fields = ['FirstName', 'LastName', 'Address', 'MaritalStatus', 'Gender',
               'Salary', 'Age', 'Interests', 'DateOfJoining', 'Designation']

    @property
    def full_name(self):
        """Concatenates first name and last name"""
        return f'{self.FirstName} {self.LastName}'

    def __str__(self):
        return self.full_name

    @staticmethod
    def get_all():
        """Equivalent of Django objects.all() - returns all objects"""
        return transform_filter_names(match_all())

    @staticmethod
    def get_by_pk(pk):
        """Return object by its id"""
        return get_by_id(pk)[0]['_source']
