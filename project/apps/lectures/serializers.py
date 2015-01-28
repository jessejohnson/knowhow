from rest_framework import serializers
from apps.core.serializers import TopicSerializer
from .models import LearningResource

class LearningResourceSerializer(serializers.HyperlinkedModelSerializer):
	topic = TopicSerializer(many=False, read_only=True)
	
	class Meta:
		model = LearningResource
		fields = ('id', 'url', 'link', 'topic' ,'summary', 'name',)