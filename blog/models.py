from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
	question 		=	models.TextField(max_length=500)
	constraints		=	models.TextField(max_length=500)
	input_Format	=	models.TextField(max_length=500)
	output_Format	=	models.TextField(max_length=500)
	example			=	models.TextField(max_length=500)
	Time 			=	models.TimeField()	
	Date 			=	models.DateField()

class Post(models.Model):
	title			=	models.CharField(max_length=100)
	article			=	models.TextField(max_length=2000)
	time_stamp		=	models.DateTimeField()
