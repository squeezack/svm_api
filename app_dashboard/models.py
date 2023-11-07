from django.db import models

# Create your models here.
class sentimen(models.Model):
    powder = models.CharField(max_length=225)
    cushion = models.CharField(max_length=225)
