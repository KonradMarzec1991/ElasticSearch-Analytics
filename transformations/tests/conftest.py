import pytest
from enum import Enum
from transformations.models import Employee


class Error(Enum):
    AGE_ERROR = 'Age must greater than 0'
    MARTIAL_ERROR = 'Unmarried or Married allowed'
    GENDER_ERROR = 'Gender must be female or male'


@pytest.fixture
def get_employee():
    return Employee(
        FirstName='Jan', LastName='Kowalski',
        Address='Smolna', MaritalStatus='UnMarried',
        Gender='Male', Salary=25000,
        Age=40, Interests='TV, Smolna',
        DateOfJoining='2010-05-12', Designation='Special Member'
    )
