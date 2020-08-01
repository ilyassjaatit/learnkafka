from django.urls import path

from account.api.views import api_detail_user_view, api_register_user_view

app_name = "account"

urlpatterns = [
    path('register/', api_register_user_view, name='register'),
    path('<pk>/', api_detail_user_view, name='detail')
]
