from rest_framework import permissions, renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import detail_route
from rest_framework.views import APIView
from .models import Test, TestQuestionTable
from .serializers import TestQuestionTableSerializer, TestSerializer

class TestViewSet(viewsets.ModelViewSet):
	queryset = Test.objects.all()
	serializer_class = TestSerializer
	permission_classes = (permissions.IsAuthenticated,)

class TestQuestionTableViewSet(viewsets.ModelViewSet):
	queryset = TestQuestionTable.objects.all()
	serializer_class = TestQuestionTableSerializer
	permission_classes = (permissions.IsAuthenticated,)

class TakeTestView(generics.ListAPIView):
	"""
	Loads a test for a student to take
	"""
	permission_classes = (permissions.IsAuthenticated,)
	serializer_class = TestQuestionTableSerializer

	def get_queryset(self):
		"""
		Retrieve all the questions belonging to a specific test
		provided by the param test_id in order
		"""
		test_id = self.request.query_params.get('test_id', None)
		queryset = TestQuestionTable.objects.filter(test_id=test_id).order_by("question_number")
		return queryset