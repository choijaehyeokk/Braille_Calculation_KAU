from django.db import models

# Create your models here.
class Braille(models.Model):
    images = models.ImageField(blank=True,upload_to ='images',null=True)