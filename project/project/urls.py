from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.core.api import router
from rest_framework.authtoken import views

# specific views
from apps.core.views import SignUpView
from apps.tests.views import TakeTestView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', views.obtain_auth_token),

    # specific views
    url(r'api/signup/', SignUpView.as_view()),
    url(r'api/taketest/', TakeTestView.as_view()),
)
