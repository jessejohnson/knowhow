from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from .serializers import UserSerializer
from .permissions import IsUserOrReadOnly

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed and edited
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (IsUserOrReadOnly,)

class SignUpView(generics.CreateAPIView):
	"""
	Allow new users to sign up
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (AllowAny,)


# class UserSignUpViewSet(viewsets.ViewSet):
# 	"""
# 	API endpoint for unauthenticated users to create user accounts
# 	"""
# 	permission_classes = (AllowAny,)

# 	def create(self, request):
# 		queryset = User.objects.all()
# 		serializer = UserSerializer
# 		user = User(username=request.data['username'], email=request.data['email'])
# 		user.set_password(request.data['password'])
# 		user.save()