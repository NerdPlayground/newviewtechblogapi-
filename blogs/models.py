from django.db import models

class Blog(models.Model):
    blog_read_time= models.IntegerField(default=10)
    blog_title= models.CharField(max_length=255)
    blog_content= models.CharField(max_length=255)
    blog_created_at= models.DateTimeField(auto_now_add=True)
    blog_updated_at= models.DateTimeField(auto_now=True)
    blog_owner= models.ForeignKey('authentication.User',related_name='blogs',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.blog_title} by {self.blog_owner}'