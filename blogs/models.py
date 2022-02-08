from django.db import models

class Blog(models.Model):
    blog_read_time= models.IntegerField(default=10)
    blog_title= models.CharField(max_length=255)
    blog_content= models.CharField(max_length=255)
    blog_created_at= models.DateTimeField(auto_now_add=True)
    blog_updated_at= models.DateTimeField(auto_now=True)
    # blog_owner= models.ForeignKey('blogs.User',on_delete=models.CASCADE)