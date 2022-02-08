from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from authentication.serializers import RegisterSerializer,LoginSerializer,UserSerializer

class UserAPIView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        user= request.user
        serializer= UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)

class RegisterAPIView(APIView):
    def post(self,request):
        data= request.data
        serializer= RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    def post(self, request):
        username= request.data.get('username')
        password= request.data.get('password')
        user= authenticate(username=username, password=password)

        if user != None:
            serializer= LoginSerializer(user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({"message":"invalid credentials"},status=status.HTTP_401_UNAUTHORIZED)