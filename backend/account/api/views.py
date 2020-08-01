from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from account.models import UserProfile
from account.api.serializers import UserProfileSerializer, RegistrationUserSerializer


@api_view(['POST', ])
def api_register_user_view(request):
    """
    Register a new user
    Codes HTTP
        If the registration has been correct return 201
        If the registration was incorrect, return 409
    curl example:
        curl --location --request POST 'http://127.0.0.1:8000/api/account/register/' \
            --header 'Content-Type: application/json' \
            --data-raw '{
                "username": "ilyassjaatit",
                "email": "ilyassjaatit@gmail.com",
                "password": "super_password"
            }'
    """
    serializer = RegistrationUserSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        data['response'] = "Successfully registered {}".format(user.username)
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        data = serializer.errors
        return Response(data, status=status.HTTP_409_CONFLICT)


@api_view(['GET', ])
def api_detail_user_view(request, pk):
    """Return user detail by pk"""
    try:
        user = UserProfile.objects.get(user__pk=pk)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializers = UserProfileSerializer(user)
    return Response(serializers.data)
