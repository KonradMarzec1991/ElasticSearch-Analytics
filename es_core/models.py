from django.db import models
from .utils import (
    upsert,
    delete_from_es
)


class Employee(models.Model):

    martial_status = (
        ('married', 'Married'),
        ('unmarried', 'Unmarried')
    )

    gender_status = (
        ('F', 'Female'),
        ('M', 'Male')
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    martial_status = models.CharField(max_length=20, choices=martial_status)
    gender = models.CharField(max_length=1, choices=gender_status)
    salary = models.BigIntegerField()
    age = models.SmallIntegerField()
    interests = models.TextField()
    date_of_joining = models.DateField()
    position = models.CharField(max_length=50)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name

    def as_elasticsearch_dict(self):
        """
        Creates ElasticSearch dict ready to use
        :return: dictionary with `class` attrs
        """
        return {
            'FirstName': self.first_name,
            'LastName': self.last_name,
            'Designation': self.position,
            'Salary': self.salary,
            'DateOfJoining': self.date_of_joining,
            'Address': self.address,
            'Gender': self.gender_status,
            'Age': self.age,
            'MaritalStatus': self.martial_status,
            'Interests': self.interests
        }

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save(force_insert=False, force_update=False, using=None,
                     update_fields=None)
        upsert(self)

    def delete(self, using=None, keep_parents=False):
        delete_from_es(self.id)
        super().delete(using=None, keep_parents=False)
