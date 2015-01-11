from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.HyperlinkedModelSerializer):

	def create(self, validated_data):
		user = User(email=validated_data['email'], username=validated_data['username'])
		user.set_password(validated_data['password'])
		user.save()
		return user
	
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups', 'password',)
		write_only_fields = ('password',)