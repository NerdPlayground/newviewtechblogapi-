from blogs.models import Blog
from rest_framework import serializers
from authentication.models import User

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
    # blogs= serializers.PrimaryKeyRelatedField(many=True,queryset=Blog.objects.all())
    # comments= serializers.PrimaryKeyRelatedField(many=True,queryset=Comment.objects.all())
    # class Meta:
    #     model= User
    #     fields= ['username','email','blogs','comments']
    blogs= serializers.PrimaryKeyRelatedField(many=True,queryset=Blog.objects.all())
    class Meta:
        model= User
        fields= ['username','email','blogs']