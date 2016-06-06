from django.shortcuts import render
from django_twilio.decorators import twilio_view
from twilio.twiml import Response
 
@twilio_view
def sms(request):
    r = Response()
    r.message('Hello from your Django app!')
    return r