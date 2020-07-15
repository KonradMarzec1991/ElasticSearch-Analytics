class TestEmployeeModel:

    def test_model_attrs(self, get_employee):
        emp = get_employee
        assert emp.full_name == 'Jan Kowalski'
        assert len(emp.__dict__) == 10
