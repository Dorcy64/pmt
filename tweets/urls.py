from django.urls import path
from rest_framework import routers
from tweets import views

router = routers.DefaultRouter()
router.register(r'tweets', views.TweetViewSet)

urlpatterns = [
    path('', views.tweet_list),
]
