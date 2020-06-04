from rest_framework.test import APIClient
from transformations.views import GeneralFilterViewSet


class TestGeneralFilteViewSet:

    def test_view_args(self):
        client = APIClient()
        response = client.get('/general/?gender=XYZT')
        assert response.status_code == 404
        print(response.data['gender'][0])
        assert 1 == 2
