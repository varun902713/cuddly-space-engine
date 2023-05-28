from rest_framework import generics
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from django.contrib.auth.models import User
import jwt
key = 'varun123'

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
from rest_framework.decorators import api_view

from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import jwt

class login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Generate JWT token
            token = jwt.encode({'user_id': user.id}, key, algorithm='HS256')

            return Response({'token': token}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def validation(request):
    token=request.POST['token']
    valid=jwt.decode(token,key=key,algorithms='HS256')
    return Response({'valid':valid})
