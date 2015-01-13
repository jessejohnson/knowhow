from rest_framework import serializers
from .models import EssayQuestion, MultipleChoiceQuestion, CaseStudy, CaseStudyQuestion

class EssayQuestionSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = EssayQuestion
		fields = ('url', 'paper', 'exam', 'question',)

class MultipleChoiceQuestionSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = MultipleChoiceQuestion
		fields = ('url', 'paper', 'exam', 'question', 'answer', 'option_a', 'option_b', 'option_c', 'option_d',)

class CaseStudySerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = CaseStudy
		fields = ('url', 'paper', 'exam', 'case',)

class CaseStudyQuestionSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = CaseStudyQuestion
		fields = ('url', 'case_study', 'paper', 'exam', 'question')