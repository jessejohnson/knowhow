from rest_framework import permissions, renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import detail_route
from rest_framework.views import APIView
from .models import Test, TestTable
from .serializers import TestTableSerializer, TestSerializer

class TestViewSet(viewsets.ModelViewSet):
	queryset = Test.objects.all()
	serializer_class = TestSerializer
	permission_classes = (permissions.IsAuthenticated,)

class TestTableViewSet(viewsets.ModelViewSet):
	queryset = TestTable.objects.all()
	serializer_class = TestTableSerializer
	permission_classes = (permissions.IsAuthenticated,)

class TakeTestView(generics.ListAPIView):
	"""
	Loads a test for a student to take
	"""
	permission_classes = (permissions.IsAuthenticated,)
	serializer_class = TestTableSerializer

	def get_queryset(self):
		"""
		Retrieve all the questions belonging to a specific test
		provided by the param test_id in order
		"""
		test_id = self.request.query_params.get('test_id', None)
		queryset = TestTable.objects.filter(test_id=test_id).order_by("question_number")
		return queryset