from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils import timezone


import os
from mptt.models import MPTTModel, TreeForeignKey
from django.utils import timezone
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import urllib
import urllib.request

from django.core.files.base import ContentFile

class Product(models.Model):
    section = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    prodType = models.CharField(max_length=50)
    prodName = models.CharField(max_length=50)
    prodUrl = models.URLField(max_length=100)
    prodProperties =  models.TextField(max_length=500)
    brand = models.CharField(max_length=20)
    imageLink = models.URLField(max_length=100)
    image = models.ImageField(max_length=500)
    price = models.FloatField()
    #availability = models.NullBooleanField(null=True)
    availability = models.CharField(max_length=20)
    discount = models.CharField(max_length=5)


    #def save(self, *args, **kwargs):
        #if self.imageLink:
            #filename = urllib.parse(self.imageLink).path.split('/')[-1]
            #img_temp = NamedTemporaryFile(delete=True)
            #img_temp.write(urllib.request.urlopen(self.imageLink).read())
            #img_temp.flush()
            #self.image = File(img_temp)

    def saveImages(self):
        """Store image locally if we have a URL"""
        if self.imageLink and not self.image:
            f= open('imageLink.txt','wb')
            f.write(bytes(str(self.imageLink), 'UTF-8'))
            f.close()
            req = urllib.request.urlopen(self.imageLink, headers={'User-Agent': 'Mozilla/5.0'})
            result = urlopen(req)
            self.image.save(os.path.basename(self.imageLink),ContentFile(result.read()))
            print ("Image saved")
            self.save()

    def __str__(self):
        return self.prodName



