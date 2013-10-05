from django.db import models
from django.conf import settings
import re
import subprocess
import os

class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True)

    def children(self):
        return Tag.objects.filter(parent=self.pk)

    def serializable_object(self):
        obj = {'name': self.name, 'children': []}
        for child in self.children():
            obj['children'].append(child.serializable_object())
        return obj


class Document(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to="documents/%Y/%m/%d")
    thumbnail = models.ImageField(upload_to="documents/thumbnails/%Y/%m/%d")
    preview = models.ImageField(upload_to="documents/previews/%Y/%m/%d")

    def save_processing(self):
        if not self.file:
            return

       
        thumbnail_path =  re.sub(r'documents/','documents/thumbnail/', os.path.split(self.file.name)[0])+"/"
        if not os.path.exists(thumbnail_path):
            os.makedirs(thumbnail_path)
        thumbnail_path += os.path.splitext(os.path.split(self.file.name)[-1])[0]+".png"
        params = ['convert', settings.MEDIA_ROOT+self.file.name+"[0]", '-resize','200', settings.MEDIA_ROOT+thumbnail_path]
        subprocess.check_call(params) 
        self.thumbnail = settings.MEDIA_URL+thumbnail_path
        self.save()
        

