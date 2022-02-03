from blogs.models import Blog
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from blogs.serializers import BlogSerializer
from rest_framework.decorators import APIView

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