from .transform_filters import transform_filter_names
from es_core.es_helpers.es_filters import match_all, get_by_id


class Employee2:
    def __init__(self, FirstName, LastName, Address, MaritalStatus, Gender,
                 Salary, Age, Interests, DateOfJoining, Designation):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Address = Address
        self.MaritalStatus = MaritalStatus
        self.Gender = Gender
        self.Salary = Salary
        self.Age = Age
        self.Interests = Interests
        self.DateOfJoining = DateOfJoining
        self.Designation = Designation

    @staticmethod
    def get_all():
        return transform_filter_names(match_all())

    @staticmethod
    def get_by_pk(pk):
        return get_by_id(pk)[0]['_source']
