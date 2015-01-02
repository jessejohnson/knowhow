from rest_framework import permissions, renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from .models import LearningContent, Topic
from .serializers import LearningContentSerializer, TopicSerializer

class LearningContentViewSet(viewsets.ModelViewSet):
	queryset = LearningContent.objects.all()
	serializer_class = LearningContentSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class TopicViewSet(viewsets.ModelViewSet):
	queryset = Topic.objects.all()
	serializer_class = TopicSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)