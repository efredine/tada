from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Channel

class ChannelListView(LoginRequiredMixin, generic.ListView):
    context_object_name = 'channel_list'
    template_name = 'channels/channel_list.html'
    
    def get_queryset(self):
        return Channel.objects.filter(users=self.request.user).order_by('name')
         
class ChannelDetailView(LoginRequiredMixin, generic.DetailView):
    model = Channel
    template_name = 'channels/channel_detail.html'
