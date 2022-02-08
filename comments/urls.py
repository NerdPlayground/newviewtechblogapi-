from django.urls import path
from comments.views import CommentAPIView, CommentDetailAPIView

urlpatterns= [
    path('comments/',CommentAPIView.as_view(),name='comment'),
    path('comments/<int:pk>/',CommentDetailAPIView.as_view(),name='comment-details'),
]