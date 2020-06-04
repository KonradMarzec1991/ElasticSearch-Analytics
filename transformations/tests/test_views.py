from rest_framework.test import APIClient
from .conftest import Error


class TestGeneralFilteViewSet:

    def test_view_gender(self):
        client = APIClient()
        response = client.get('/general/?gender=XYZT')
        assert response.status_code == 404
        assert response.data['gender'][0] == Error.GENDER_ERROR.value

        response = client.get('/general/?gender=Male')
        assert response.status_code == 200

    def test_view_martial_status(self):
        client = APIClient()
        response = client.get('/general/?martial_status=abcdef')
        assert response.status_code == 404
        assert response.data['martial_status'][0] == Error.MARTIAL_ERROR.value

        response = client.get('/general/?martial_status=Married')
        assert response.status_code == 200

    def test_view_age(self):
        client = APIClient()
        response = client.get('/general/?age=-50')
        assert response.status_code == 404
        assert response.data['age'][0] == Error.AGE_ERROR.value

        response = client.get('/general/?age=35')
        assert response.status_code == 200


