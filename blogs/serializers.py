from rest_framework import serializers
from blogs.models import Blog,Comment,User

class BlogSerializer(serializers.ModelSerializer):
    comments= serializers.PrimaryKeyRelatedField(many=True,queryset=Comment.objects.all())
    class Meta:
        model= Blog
        fields=['id','blog_owner','blog_created_at','blog_read_time','blog_title','blog_content','comments']
        read_only_fields= ['blog_owner']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comment
        fields=['id','comment_created_at','comment_under','comment_owner','comment_content']
        read_only_fields= ['comment_owner']

class RegisterSerializer(serializers.ModelSerializer):
    password= serializers.CharField(max_length=20,min_length=8,write_only=True)
    class Meta:
        model= User
        fields= ['username','email','password']
    
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    password= serializers.CharField(max_length=20,min_length=8,write_only=True)
    class Meta:
        model= User
        fields= ['username','password','token']
        read_only_fields= ['token']

class UserSerializer(serializers.ModelSerializer):
    blogs= serializers.PrimaryKeyRelatedField(many=True,queryset=Blog.objects.all())
    comments= serializers.PrimaryKeyRelatedField(many=True,queryset=Comment.objects.all())
    class Meta:
        model= User
        fields= ['username','email','blogs','comments']