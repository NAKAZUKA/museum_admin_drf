from django.shortcuts import render
from rest_framework import viewsets, mixins, generics

from main_app.models import Post, Answer, Question, Exhibit
from .serializers import PostSerializer, AnswerSerializer, QuestionSerializer, ExhibitSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        exhibit_slug = self.request.query_params.get('exhibit_slug', None)
        if exhibit_slug is not None:
            queryset = queryset.filter(exhibit__slug=exhibit_slug)
        return queryset


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_queryset(self):
        queryset = Answer.objects.all()
        question_slug = self.request.query_params.get('question_slug', None)
        if question_slug is not None:
            queryset = queryset.filter(question__slug=question_slug)
        return queryset


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        queryset = Question.objects.all()
        exhibit_slug = self.request.query_params.get('exhibit_slug', None)
        if exhibit_slug is not None:
            queryset = queryset.filter(exhibit__slug=exhibit_slug)
        return queryset


class ExhibitViewSet(viewsets.ModelViewSet):
    queryset = Exhibit.objects.all()
    serializer_class = ExhibitSerializer

    def get_queryset(self):
        queryset = Exhibit.objects.all()
        exhibit_slug = self.request.query_params.get('exhibit_slug', None)
        if exhibit_slug is not None:
            queryset = queryset.filter(slug=exhibit_slug)
        return queryset
