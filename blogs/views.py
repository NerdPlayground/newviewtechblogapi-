from django.http import Http404
from rest_framework import status
from blogs.models import Blog,Comment
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from blogs.serializers import BlogSerializer,CommentSerializer,RegisterSerializer,LoginSerializer

class UserAPIView(APIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    def get(self,request):
        user= request.user
        serializer= RegisterSerializer(user)
        return Response({'user':serializer.data},status=status.HTTP_200_OK)

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

class BlogAPIView(APIView):
    def get(self,request):
        blogs= Blog.objects.all()
        serializer= BlogSerializer(blogs,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        data= request.data
        serializer= BlogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class BlogDetailAPIView(APIView):
    def get_object(self,pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        blog= self.get_object(pk)
        serializer= BlogSerializer(blog)
        return Response(serializer.data)

    def put(self,request,pk):
        blog= self.get_object(pk)
        serializer= BlogSerializer(blog,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        blog= self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentAPIView(APIView):
    def get(self,request):
        blogs= Comment.objects.all()
        serializer= CommentSerializer(blogs,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        data= request.data
        serializer= CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class CommentDetailAPIView(APIView):
    def get_object(self,pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        blog= self.get_object(pk)
        serializer= CommentSerializer(blog)
        return Response(serializer.data)

    def put(self,request,pk):
        blog= self.get_object(pk)
        serializer= CommentSerializer(blog,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        blog= self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)