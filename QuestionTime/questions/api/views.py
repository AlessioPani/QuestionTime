from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from questions.models import Answer, Question
from .serializers import AnswerSerializer, QuestionSerializer
from .permissions import IsAuthorOrReadOnly


class AnswerCreateAPIView(generics.CreateAPIView):
    '''
    REST View used by an user in order to answer a specific question.

    * Overwritten the perform_create method (inherited from GenericAPIView)
      to save the Answer serializer with all of the required attributes.
    '''
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        question = get_object_or_404(Question, slug=kwarg_slug)

        if question.answers.filter(author=request_user).exists():
            raise ValidationError("You've already answered to this question")
        else:
            serializer.save(author=request_user, question=question)


class AnswerLikeAPIView(APIView):
    '''
    REST View used by an user to add or remove a like to an answer.

    * Overwritten delete and post built-in methods.
    '''
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        user = self.request.user
        answer.voters.remove(user)
        answer.save()
        serializer_context = {"request": request}
        serializer = self.serializer_class(answer, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        user = self.request.user
        answer.voters.add(user)
        answer.save()
        serializer_context = {"request": request}
        serializer = self.serializer_class(answer, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AnswerRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    '''
    Full CRUD REST View for the Answer model.
    '''
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


class QuestionAnswerListAPIView(generics.ListAPIView):
    '''
    REST View used to retrieve all the answers for a specific question,
    identified by its slug.
    '''
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("slug")
        return Answer.objects.filter(question__slug=kwarg_slug)


class QuestionViewSet(viewsets.ModelViewSet):
    '''
    REST View used to retrieve all the questions written by a specific
    user.
    '''
    queryset = Question.objects.all().order_by("-created_at")
    lookup_field = "slug"
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
