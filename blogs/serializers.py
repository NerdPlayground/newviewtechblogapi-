from rest_framework import serializers
from blogs.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    # comments= serializers.PrimaryKeyRelatedField(many=True,queryset=Comment.objects.all())
    # class Meta:
    #     model= Blog
    #     fields=['id','blog_owner','blog_created_at','blog_read_time','blog_title','blog_content','comments']
    #     read_only_fields= ['blog_owner']
    # comments= serializers.PrimaryKeyRelatedField(many=True,queryset=Comment.objects.all())
    class Meta:
        model= Blog
        fields=['id','blog_owner','blog_created_at','blog_read_time','blog_title','blog_content']
        read_only_fields= ['blog_owner']