from rest_framework import serializers
from .models import LearningResource

class LearningResourceSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = LearningResource
		fields = ('url', 'link', 'topic' ,'summary', 'name', 'slug',)