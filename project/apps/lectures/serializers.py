from rest_framework import serializers
from .models import LearningContent, Topic

class LearningContentSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = LearningContent
		fields = ('link', 'topic' ,'summary', 'name', 'slug',)

class TopicSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Topic
		fields = ('summary', 'name', 'slug',)