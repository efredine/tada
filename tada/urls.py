from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^channels/', include('channels.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'channels/login.html'}),
    url(r'^accounts/logout/$', auth_views.logout_then_login, name='logout'),
]
