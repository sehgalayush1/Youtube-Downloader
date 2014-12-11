from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.http import *
from django.conf import settings
# import mongoengine
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
import random,string
from djangoaudio.models import * 
import pafy

def home(request):
	c = {}
	c.update(csrf(request))
	if request.GET:
		search = request.GET.get('search')
		if search:
			video = pafy.new(url)
			streams = video.streams
			return render_to_response('result.html',{'s':streams,'video':video},context_instance=RequestContext(request))
	return render_to_response('index.html')