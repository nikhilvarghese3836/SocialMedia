from django.urls import path
from .views import AddPostAPIView, GetPostFeedAPIView
urlpatterns = [
  path("new",AddPostAPIView.as_view()),
  path("feed",GetPostFeedAPIView.as_view())
]
