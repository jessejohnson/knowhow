from rest_framework import permissions, renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from .models import EssayQuestion, MultipleChoiceQuestion, CaseStudy, CaseStudyQuestion
from .serializers import EssayQuestionSerializer, MultipleChoiceQuestionSerializer, CaseStudySerializer, CaseStudyQuestionSerializer

class EssayQuestionViewSet(viewsets.ModelViewSet):
	queryset = EssayQuestion.objects.all()
	serializer_class = EssayQuestionSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class MultipleChoiceQuestionViewSet(viewsets.ModelViewSet):
	queryset = MultipleChoiceQuestion.objects.all()
	serializer_class = MultipleChoiceQuestionSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CaseStudyViewSet(viewsets.ModelViewSet):
	queryset = CaseStudy.objects.all()
	serializer_class = CaseStudySerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CaseStudyQuestionViewSet(viewsets.ModelViewSet):
	queryset = CaseStudyQuestion.objects.all()
	serializer_class = CaseStudyQuestionSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)