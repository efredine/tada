from django import forms

class ChannelPostForm(forms.Form):
    post = forms.CharField(max_length=200, label='Post something')