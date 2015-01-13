from rest_framework import permissions, renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from .models import Test, TestTable
from .serializers import TestTableSerializer, TestSerializer

class TestViewSet(viewsets.ModelViewSet):
	queryset = Test.objects.all()
	serializer_class = TestSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class TestTableViewSet(viewsets.ModelViewSet):
	queryset = TestTable.objects.all()
	serializer_class = TestTableSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)