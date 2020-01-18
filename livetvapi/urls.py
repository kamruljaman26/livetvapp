#My Import
from livetvapi import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tvlink',views.LiveTvViewSet)

urlpatterns = [
    path('', include(router.urls)),
]