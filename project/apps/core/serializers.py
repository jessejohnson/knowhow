from rest_framework import serializers
from .models import Topic, Exam, Paper, User

class UserSerializer(serializers.HyperlinkedModelSerializer):

	def create(self, validated_data):
		user = User(email=validated_data['email'], username=validated_data['username'])
		user.set_password(validated_data['password'])
		user.save()
		return user
	
	class Meta:
		model = User
		fields = ('id', 'url', 'username', 'email', 'password', 'avatar')
		write_only_fields = ('password',)

class TopicSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Topic
		fields = ('id', 'url', 'name',)

class ExamSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Exam
		fields = ('id', 'url', 'name', 'short_name',)

class PaperSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Paper
		fields = ('id', 'url', 'name', 'code',)