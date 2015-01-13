from rest_framework import permissions, renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from .models import StudentRecord
from .serializers import StudentRecordSerializer

class StudentRecordViewSet(viewsets.ModelViewSet):
	queryset = StudentRecord.objects.all()
	serializer_class = StudentRecordSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)