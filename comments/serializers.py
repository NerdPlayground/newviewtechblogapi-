from rest_framework import serializers
from comments.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        # model= Comment
        # fields=['id','comment_created_at','comment_under','comment_owner','comment_content']
        # read_only_fields= ['comment_owner']
        model= Comment
        fields=['id','comment_created_at','comment_content']