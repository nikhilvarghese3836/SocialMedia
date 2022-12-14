from django.urls import path
from .views import UserDetailAPI, RegisterUserAPIView, UserFollowAPIView, UserUnfollowAPIView
urlpatterns = [
  path("get-details",UserDetailAPI.as_view()),
  path('register',RegisterUserAPIView.as_view()),
  path('follow',UserFollowAPIView.as_view()),
  path('unfollow',UserUnfollowAPIView.as_view()),
]

