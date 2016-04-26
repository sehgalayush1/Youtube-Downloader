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
import random, string
import pafy
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def home(request):
	c = {}
	c.update(csrf(request))
	if request.GET:
		url = request.GET.get('url')
		if url:
			validate = URLValidator()
			try:
				validate(url)
				video = pafy.new(url)
				streams = video.streams
				f = open('getlist.txt','a')
				f.write(str(url)+'\n')
				f.close()
				print "\n \n \n############ The details of the Video are as follows: ########### \n"
				print "Title : %s\n"%(video.title)
				print "Author : %s\n"%(video.author)
				print "Length : %s seconds\n"%(video.length)
				print "No. of views : %s \n"%(video.viewcount)
				for s in streams:
					print " Link to Video : %s"%(s.url)
					print 
					print
				print "#################################################################\n \n \n"
				return render_to_response('result.html')
			except ValidationError:
			    return render(request, 'index.html', {'error':'Please enter a valid url!'})
			
	return render_to_response('index.html')

def analytics(request):
	"""
	Analytics part is in progress right now. 
	"""
	try:
		c = {}
		c.update(csrf(request))
		if request.GET:
			search = request.GET.get('search')
			if search:
				cc1=video.objects.filter(videoName__icontains=search)
				cc2=video.objects.filter(title__icontains=search)
				cc3=video.objects.filter(author__icontains=search)
			return render_to_response('result.html',{'cc1':cc1,'cc2':cc2,'cc3':cc3},context_instance=RequestContext(request))
		return render_to_response('index.html')
	except:
		return HttpResponse("<h1>Under Construction... Will be there very soon </h1>")

def video(request):
	# a = None
	a = video.objects.all()
	return render_to_response('index.html',{'a':a},context_instance=RequestContext(request))

