from django.db import models

# Create your models here.
class ingredients(models.Model):
    name = models.CharField(max_length= 64, blank=False)

class ingredients_in_coctail(models.Model):
    id_coctail = models.IntegerField(blank=False)
    id_ingredient = models.IntegerField(blank=False)
    Amount = models.CharField(max_length=20, blank=False)

class cocteil (models.Model):
    name = models.CharField(max_length=32, blank=False)
    description = models.CharField(max_length=1024, blank=False)
    picture = models.ImageField(blank=False)