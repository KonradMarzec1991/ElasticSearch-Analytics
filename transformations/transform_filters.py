from es_core.es_helpers.es_filters import filter_by_fn
from es_core.models import Employee


print(filter_by_fn('ELVA')[0]['_source'])
print(filter_by_fn('ELVA')[0])


def transform_filter_names(es_input):
    source, result = es_input[0]['_source'], []
    for emp in source:
        result.append(Employee(
            first_name=emp['FirstName'],
            last_name=emp['LastName'],
            address=emp['Address'],
            martial_status=emp['MaritalStatus'],
            gender=emp['Gender'],
            salary=emp['Salary'],
            age=emp['Age'],
            interests=emp['Interests'],
            date_of_joining=emp['DateOfJoining'],
            position=emp['Designation'],
        ))
    return result

