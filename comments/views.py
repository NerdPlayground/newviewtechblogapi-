from django.http import Http404
from rest_framework import status
from comments.models import Comment
from rest_framework.response import Response
from rest_framework.decorators import APIView
from comments.serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated

class CommentAPIView(APIView):
    permission_classes= [IsAuthenticated]

    def get(self,request):
        comments= Comment.objects.all()
        serializer= CommentSerializer(comments,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        data= request.data
        serializer= CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save(comment_owner=self.request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class CommentDetailAPIView(APIView):
    permission_classes= [IsAuthenticated]

    def get_object(self,pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        comment= self.get_object(pk)
        serializer= CommentSerializer(comment)
        return Response(serializer.data)

    def put(self,request,pk):
        comment= self.get_object(pk)
        serializer= CommentSerializer(comment,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        comment= self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)