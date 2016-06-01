from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

@python_2_unicode_compatible
class Channel(models.Model):
    users = models.ManyToManyField(User)
    name = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
@python_2_unicode_compatible
class Post(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_text = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        return self.post_text