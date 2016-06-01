from django.shortcuts import render
from django.views import generic

from .models import Channel

class ChannelListView(generic.ListView):
    context_object_name = 'channel_list'
    queryset = Channel.objects.all()
    template_name = 'channels/channel_list.html'
    
class ChannelDetailView(generic.DetailView):
    model = Channel
    template_name = 'channels/channel_detail.html'
