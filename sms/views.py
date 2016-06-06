from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
 
@csrf_exempt
def sms(request):
    twiml = '<Response><Message>Hello from your Django app!</Message></Response>'
    return HttpResponse(twiml, content_type='text/xml')
