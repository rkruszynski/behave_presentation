from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
    url(r'^app/?$', views.base, name='base'),
    url(r'^foo/?$', views.foo, name='foo'),
    url(r'^new_user/?$', views.new_user, name='new_user'),
    url(r'^logs/?$', views.history_view, name='history'),
    url(r'^clear_logs/?$', views.clear_logs, name='clear_logs'),
    url(r'^unauthorized/?$', views.unauthorized, name='unauthorized'),
    url(r'^user_profile/(?P<user_id>[0-9]+)$', views.user_profile, name='user_profile'),
    url(r'^$', login, {
        'template_name': 'app/login.html'
    }, name='login')
]
