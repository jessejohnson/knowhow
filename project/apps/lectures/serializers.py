from rest_framework import serializers
from .models import LearningResource

class LearningResourceSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = LearningResource
		fields = ('id', 'url', 'link', 'topic' ,'summary', 'name',)