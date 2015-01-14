from rest_framework import serializers
from .models import StudentRecord

class StudentRecordSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = StudentRecord
		fields = ('id', 'url', 'user', 'test' ,'grade', 'name', 'slug',)