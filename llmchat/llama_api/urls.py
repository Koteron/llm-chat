from django.urls import path
from .views import MessageView, ConversationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('conversation', ConversationViewSet, basename="conversation")

urlpatterns = [
    *router.urls,
    path('message/', MessageView.as_view()),
]
