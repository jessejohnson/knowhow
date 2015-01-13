from rest_framework import serializers
from apps.questions.serializers import MultipleChoiceQuestionSerializer
from .models import Test, TestTable

class TestSerializer(serializers.HyperlinkedModelSerializer):
	

	class Meta:
		model = Test
		fields = ('id', 'url', 'exam', 'topic' ,'paper', 'name', 'slug',)

class TestTableSerializer(serializers.HyperlinkedModelSerializer):
	question = MultipleChoiceQuestionSerializer(many=False, read_only=True)

	class Meta:
		model = TestTable
		fields = ('id', 'url', 'test', 'question' ,'question_number', 'name', 'slug',)