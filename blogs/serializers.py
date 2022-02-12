from blogs.models import Blog
from comments.models import Comment
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    comments= serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    blog_owner= serializers.ReadOnlyField(source='blog_owner.username')
    class Meta:
        model= Blog
        fields=['id','blog_owner','blog_created_at','blog_read_time','blog_title','blog_content','comments']
        # read_only_fields= ['blog_owner']