from rest_framework import serializers
from blogs.models import Blog, Comment

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model= Blog
        fields=['id','blog_created_at','blog_read_time','blog_title','blog_content']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comment
        fields=['id','comment_created_at','comment_content']