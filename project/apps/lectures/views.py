from rest_framework import permissions, renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from .models import LearningResource
from .serializers import LearningResourceSerializer

class LearningResourceViewSet(viewsets.ModelViewSet):
	queryset = LearningResource.objects.all()
	serializer_class = LearningResourceSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)