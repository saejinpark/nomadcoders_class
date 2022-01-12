from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    
    created = models.DateTimeField();
    updated = models.DateTimeField();
    class Meta:
        abstract = True