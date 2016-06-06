from django.conf.urls import url
from . import views

app_name = 'sms'
urlpatterns = [
    # ex: /sms/
    url(r'^$', views.sms),
]
