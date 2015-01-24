# from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from .serializers import UserSerializer, TopicSerializer, ExamSerializer, PaperSerializer
from .models import Topic, Exam, Paper, User
from .permissions import IsUserOrReadOnly

# Create your views here.
class IndexTemplateView(TemplateView):
	"""index of prepGH"""

	template_name = "index.html"

	# def get_context_data(self, **kwargs):
	# 	context = super(IndexTemplateView, self).get_context_data(**kwargs)
	# 	try:
	# 		context['choir'] = Choir.objects.latest('modified')
	# 		context['concert'] = Concert.objects.latest('time')
	# 		context['column'] = Column.objects.latest('created')
	# 	except Exception, e:
	# 		pass
	# 	return context


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

class GetUserView(generics.RetrieveAPIView):
	"""
	Get a single user instance based on email
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (IsAuthenticated,)

	def get_object(self):
		queryset = self.get_queryset()
		email = self.request.query_params.get('email')
		user = get_object_or_404(queryset, email=email)
		return user

class TopicViewSet(viewsets.ModelViewSet):
	queryset = Topic.objects.all()
	serializer_class = TopicSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)

class ExamViewSet(viewsets.ModelViewSet):
	queryset = Exam.objects.all()
	serializer_class = ExamSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)

class PaperViewSet(viewsets.ModelViewSet):
	queryset = Paper.objects.all()
	serializer_class = PaperSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)

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