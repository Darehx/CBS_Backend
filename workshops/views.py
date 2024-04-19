from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer


@api_view(['POST'])
def login(request):
    try:
        user = User.objects.get(username=request.data['username'])
    except User.DoesNotExist:
        return Response({"error": "Invalid username"}, status=status.HTTP_400_BAD_REQUEST)

    if not user.check_password(request.data['password']):
        return Response({"error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)

    # Create a token and get or create a new one if it already exists
    token, created = Token.objects.get_or_create(user=user)

    # Serialize user data
    serializer = UserSerializer(instance=user)

    # **Add code to create and set the cookie:**
    if created:  # Only create cookie if a new token is generated
        response = Response({"auth_token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)
        # Set cookie attributes (adjust as needed)
        response.set_cookie('sessionid', token.key, max_age=3600, httponly=True)  # Secure cookie
        return response
    else:
        # Existing token, just return the response without creating a new cookie
        return Response({"auth_token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)

