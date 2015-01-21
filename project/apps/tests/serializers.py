from rest_framework import serializers
from apps.questions.serializers import MultipleChoiceQuestionSerializer
from apps.core.serializers import ExamSerializer, TopicSerializer, PaperSerializer
from .models import Test, TestTable

class TestSerializer(serializers.HyperlinkedModelSerializer):	
	exam = ExamSerializer(many=False, read_only=True)
	topic = TopicSerializer(many=False, read_only=True)
	paper = PaperSerializer(many=False, read_only=True)

	class Meta:
		model = Test
		fields = ('id', 'url', 'exam', 'topic' ,'paper', 'name', 'slug',)

class TestTableSerializer(serializers.HyperlinkedModelSerializer):
	question = MultipleChoiceQuestionSerializer(many=False, read_only=True)

	class Meta:
		model = TestTable
		fields = ('id', 'url', 'test', 'question' ,'question_number', 'name', 'slug',)