from transformations.serializers import GeneralFilterSerializer
from .conftest import Error


class TestGeneralFilterSerializer:

    def test_when_age_below_0(self):
        serializer = GeneralFilterSerializer(data={'age': -40})
        assert not serializer.is_valid()
        assert serializer.errors['age'][0] == Error.AGE_ERROR.value

    def test_when_incorrect_martial_status(self):
        serializer = GeneralFilterSerializer(data={'martial_status': 'xyzt'})
        assert not serializer.is_valid()
        assert serializer.errors['martial_status'][0] == Error.MARTIAL_ERROR.value

    def test_when_incorrect_gender(self):
        serializer = GeneralFilterSerializer(data={'gender': 'abcdef'})
        assert not serializer.is_valid()
        assert serializer.errors['gender'][0] == Error.GENDER_ERROR.value
