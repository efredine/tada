from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin

from .models import Channel

class ChannelHasUserMixin(AccessMixin):
    """
    Mixin for the channel detail view which verifies the channel has the current user.
    """
    
    raise_exception = True
    permission_denied_message = "You don't have access to this channel."
          
    def channel_has_user(self, channel):
        return self.request.user in channel.users.all()
    
    def get_object(self):
        retrieved_object = super(ChannelHasUserMixin, self).get_object()
        if self.channel_has_user(retrieved_object):
            return retrieved_object
        else:
            self.handle_no_permission()

class ChannelListView(LoginRequiredMixin, generic.ListView):
    context_object_name = 'channel_list'
    template_name = 'channels/channel_list.html'
    
    def get_queryset(self):
        return Channel.objects.filter(users=self.request.user).order_by('name')
         
class ChannelDetailView(LoginRequiredMixin,  ChannelHasUserMixin, generic.DetailView):
    model = Channel
    template_name = 'channels/channel_detail.html'
