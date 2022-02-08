from django.urls import path
from authentication.views import RegisterAPIView,LoginAPIView,UserAPIView

urlpatterns= [
    path('user/',UserAPIView.as_view(),name='user'),
    path('register/',RegisterAPIView.as_view(),name='register'),
    path('login/',LoginAPIView.as_view(),name='login')
]