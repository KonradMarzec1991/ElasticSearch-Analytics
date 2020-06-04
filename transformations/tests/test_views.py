from rest_framework.test import APIClient
from transformations.views import GeneralFilterViewSet
from .conftest import Error


class TestGeneralFilteViewSet:

    def test_view_args(self):
        client = APIClient()
        response = client.get('/general/?gender=XYZT')
        assert response.status_code == 404
        assert response.data['gender'][0] == Error.GENDER_ERROR.value
