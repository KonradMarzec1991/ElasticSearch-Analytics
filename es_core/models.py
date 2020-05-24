from django.db import models
from .utils import (
    upsert,
    delete_from_es
)

from .es_helpers.es_filters import get_by_id


class ElasticSearchManager(models.Manager):
    def es_get_by_pk(self, pk):
        return get_by_id(pk)[0]['_source']


class Employee(models.Model):

    martial_status = (
        ('Married', 'Married'),
        ('Unmarried', 'Unmarried')
    )

    gender_status = (
        ('Female', 'Female'),
        ('Male', 'Male')
    )

    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Address = models.CharField(max_length=150)
    MaritalStatus = models.CharField(max_length=20, choices=martial_status)
    Gender = models.CharField(max_length=10, choices=gender_status)
    Salary = models.BigIntegerField()
    Age = models.SmallIntegerField()
    Interests = models.TextField()
    DateOfJoining = models.DateField()
    Designation = models.CharField(max_length=50)

    es_object = ElasticSearchManager()

    @property
    def full_name(self):
        return f'{self.FirstName} {self.LastName}'

    def __str__(self):
        return self.full_name

    def as_elasticsearch_dict(self):
        """
        Creates ElasticSearch dict ready to use
        :return: dictionary with `class` attrs
        """
        return {
            'id': self.id,
            'FirstName': self.FirstName,
            'LastName': self.LastName,
            'Designation': self.Designation,
            'Salary': self.Salary,
            'DateOfJoining': self.DateOfJoining,
            'Address': self.Address,
            'Gender': self.Gender,
            'Age': self.Age,
            'MaritalStatus': self.MaritalStatus,
            'Interests': self.Interests
        }

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save(force_insert=False, force_update=False, using=None,
                     update_fields=None)
        upsert(self)

    def delete(self, using=None, keep_parents=False):
        delete_from_es(self.id)
        super().delete(using=None, keep_parents=False)
