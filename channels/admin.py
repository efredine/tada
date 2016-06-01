from django.contrib import admin

from .models import Channel, Post

admin.site.register(Channel)
admin.site.register(Post)