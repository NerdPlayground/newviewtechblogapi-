from blogs.models import Blog
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model= Blog
        fields=['id','blog_created_at','blog_read_time','blog_title','blog_content']