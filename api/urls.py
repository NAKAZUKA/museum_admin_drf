from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    AnswerViewSet,
    ExhibitViewSet,
    PostViewSet,
    QuestionViewSet
)


router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('exhibits', ExhibitViewSet, basename='exhibits')
router.register('questions', QuestionViewSet, basename='questions')
router.register('answers', AnswerViewSet, basename='answers')

urlpatterns = [
    path('', include(router.urls)),
]
