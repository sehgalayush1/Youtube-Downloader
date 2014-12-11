from django.db import models
# from djangotoolbox import *

class songs(models.Model):
	title = models.CharField(max_length = 2000,default = None)
	url =  models.CharField(max_length = 2000,default = None)#ListField()
	songName =  models.CharField(max_length = 2000,default = None)#ListField()
	author =  models.CharField(max_length = 2000,default = None)#ListField()
	# ziplink =  models.CharField()#ListField()