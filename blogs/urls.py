from django.urls import path
from blogs.views import (
    BlogAPIView,BlogDetailAPIView,CommentAPIView,
    CommentDetailAPIView,RegisterAPIView,LoginAPIView,UserAPIView
)

urlpatterns= [
    path('user/',UserAPIView.as_view(),name='user'),
    path('register/',RegisterAPIView.as_view(),name='register'),
    path('login/',LoginAPIView.as_view(),name='login'),
    path('blogs/',BlogAPIView.as_view(),name='blogs'),
    path('blogs/<int:pk>/',BlogDetailAPIView.as_view(),name='blog-details'),
    path('comments/',CommentAPIView.as_view(),name='comment'),
    path('comments/<int:pk>/',CommentDetailAPIView.as_view(),name='comment-details'),
]