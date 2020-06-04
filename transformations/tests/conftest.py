import pytest

from transformations.models import Employee


@pytest.fixture
def get_employee():
    return Employee(
        FirstName='Jan', LastName='Kowalski',
        Address='Smolna', MaritalStatus='UnMarried',
        Gender='Male', Salary=25000,
        Age=40, Interests='TV, Smolna',
        DateOfJoining='2010-05-12', Designation='Special Member'
    )
