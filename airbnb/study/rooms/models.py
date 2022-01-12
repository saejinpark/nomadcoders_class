from django.db import models
from django_countries.fields import CountryField
from core import models as core_models

# Create your models here.
class Room(core_models.TimeStampedModel):
    
    name = models.ChaeField(max_lenght=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = model.CharField(max_length=140)
    bed = models.IntergerField()