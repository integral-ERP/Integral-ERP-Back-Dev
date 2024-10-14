from rest_framework.views import APIView
from user.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from user.api.serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer
from user. models import User

class RegisterView(APIView):
    def post(self, request):
        # print('Registrando Usuario...')
        # return Response(status=status.HTTP_200_OK, data="OKKKK")
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
             
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    permission_classes = [ IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
        
    def put(self, request):
        user = User.objects.get (id=request.user.id)
        serializer = UserUpdateSerializer(user, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)