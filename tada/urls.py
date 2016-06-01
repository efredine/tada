from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^channels/', include('channels.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
