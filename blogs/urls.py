from django.urls import path
from blogs.views import BlogAPIView, BlogDetailAPIView,CommentAPIView,CommentDetailAPIView

urlpatterns= [
    path('blogs/',BlogAPIView.as_view(),name='blogs'),
    path('blogs/<int:pk>/',BlogDetailAPIView.as_view(),name='blog-details'),
    path('comment/',CommentAPIView.as_view(),name='comment'),
    path('comment/<int:pk>/',CommentDetailAPIView.as_view(),name='comment-details'),
]