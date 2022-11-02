from django.db import models
from django.forms import FileField
from tinymce.models import HTMLField
from  embed_video.fields  import  EmbedVideoField

# creating the models for python  bloging page

class project(models.Model):
    Project_name = models.CharField( max_length=50)
    project_images = models.FileField(upload_to ="media", max_length=250, null =False, default= None)
    project_id = models.IntegerField(primary_key=True)
    project_date =models.CharField(max_length=50)
    project_heading = models.TextField()
    project_half = models.TextField(null = False, default=None) 
    project_blogimage = models.FileField(upload_to ="media",max_length=250,null =False, default= None)
    project_content =HTMLField()
    project_video = EmbedVideoField(null = False) 


class hardware(models.Model):
    Project_name = models.CharField( max_length=50)
    project_images = models.FileField(upload_to ="media", max_length=250, null =False, default= None)
    project_id = models.IntegerField(primary_key=True)
    project_date =models.CharField(max_length=50)
    project_heading = models.TextField()
    project_half = models.TextField(null = False, default=None) 
    project_blogimage = models.FileField(upload_to ="media",max_length=250,null =False, default= None)
    project_content =HTMLField()
    project_video = EmbedVideoField(null = False)

    