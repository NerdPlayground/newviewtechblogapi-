from rest_framework import serializers
from comments.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    comment_owner= serializers.ReadOnlyField(source='comment_owner.username')
    class Meta:
        model= Comment
        fields=['id','comment_created_at','comment_owner','comment_under','comment_content']
        # read_only_fields= ['comment_owner']