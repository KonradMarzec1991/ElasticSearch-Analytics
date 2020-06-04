from transformations.serializers import GeneralFilterSerializer


class TestGeneralFilterSerializer:

    AGE_ERROR = 'Age must greater than 0'
    MARTIAL_ERROR = 'Unmarried or Married allowed'
    GENDER_ERROR = 'Gender must be female or male'

    def test_when_age_below_0(self):
        serializer = GeneralFilterSerializer(data={'age': -40})
        assert not serializer.is_valid()
        assert serializer.errors['age'][0] == self.AGE_ERROR

    def test_when_incorrect_martial_status(self):
        serializer = GeneralFilterSerializer(data={'martial_status': 'xyzt'})
        assert not serializer.is_valid()
        assert serializer.errors['martial_status'][0] == self.MARTIAL_ERROR

    def test_when_incorrect_gender(self):
        serializer = GeneralFilterSerializer(data={'gender': 'abcdef'})
        assert not serializer.is_valid()
        assert serializer.errors['gender'][0] == self.GENDER_ERROR