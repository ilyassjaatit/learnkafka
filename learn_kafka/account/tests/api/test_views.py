import pytest
from django.urls import reverse
from rest_framework import status

from account.api.views import api_detail_user_view

@pytest.mark.django_db
@pytest.mark.urls('account.api.urls')
def test_api_detail_user_view_error_not_fond(client):
    url = reverse('detail', kwargs={'pk': 9999999999999999})
    response = client.get(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND

