from django.conf.urls import url
from . import views

app_name = 'channels'
urlpatterns = [
    # ex: /channels/
    url(r'^$', views.ChannelListView.as_view(), name='channel_list'),
    # ex: /channels/5/
    url(r'^(?P<pk>[0-9]+)/$', views.ChannelDetailView.as_view(), name='channel_detail'),
]
