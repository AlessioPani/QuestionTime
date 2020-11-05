from django.urls import include, path
from .views import (AnswerCreateAPIView,
                    AnswerLikeAPIView,
                    AnswerRUDAPIView,
                    QuestionAnswerListAPIView,
                    QuestionViewSet)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"questions", QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('questions/<slug:slug>/answer/',
         AnswerCreateAPIView.as_view(),
         name="create-answer"),
    path('questions/<slug:slug>/answers/',
         QuestionAnswerListAPIView.as_view(),
         name="answers_list"),
    path('answers/<int:pk>/',
         AnswerRUDAPIView.as_view(),
         name="answer-detail"),
    path('answers/<int:pk>/like/',
         AnswerLikeAPIView.as_view(),
         name="answer-like"),
]
