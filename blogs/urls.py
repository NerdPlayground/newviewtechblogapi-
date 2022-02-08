from django.urls import path
from blogs.views import BlogAPIView,BlogDetailAPIView

urlpatterns= [
    path('blogs/',BlogAPIView.as_view(),name='blogs'),
    path('blogs/<int:pk>/',BlogDetailAPIView.as_view(),name='blog-details')
]