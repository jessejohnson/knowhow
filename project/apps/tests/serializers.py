from rest_framework import serializers
from .models import Test, TestTable

class TestSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Test
		fields = ('url', 'exam', 'topic' ,'paper', 'name', 'slug',)

class TestTableSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = TestTable
		fields = ('url', 'test', 'question' ,'question_number', 'name', 'slug',)