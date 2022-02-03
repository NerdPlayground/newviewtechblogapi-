from django.db import models

class Blog(models.Model):
    blog_created_at= models.DateTimeField(auto_now_add=True)
    blog_updated_at= models.DateTimeField(auto_now=True)
    blog_read_time= models.IntegerField(default=10)
    blog_title= models.CharField(max_length=255)
    blog_content= models.CharField(max_length=255)

class Comment(models.Model):
    comment_created_at= models.DateTimeField(auto_now_add=True)
    comment_updated_at= models.DateTimeField(auto_now=True)
    comment_content= models.CharField(max_length=255)