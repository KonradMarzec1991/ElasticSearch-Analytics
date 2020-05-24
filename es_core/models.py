from django.db import models


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
        return self.first_name


