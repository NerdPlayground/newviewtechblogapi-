from django.db import models

class Comment(models.Model):
    comment_content= models.CharField(max_length=255)
    # comment_under= models.ForeignKey('blogs.Blog',on_delete=models.CASCADE)
    # comment_owner= models.ForeignKey('blogs.User',on_delete=models.CASCADE)
    comment_created_at= models.DateTimeField(auto_now_add=True)
    comment_updated_at= models.DateTimeField(auto_now=True)