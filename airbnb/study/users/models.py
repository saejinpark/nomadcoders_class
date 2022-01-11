from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    
    """ Custon User Model """
    
    GENDER_MALE = "male"
    GERDER_FEMAIL = "female"
    GENDER_OTHER = "other"
    
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GERDER_FEMAIL, "Female"),
        (GENDER_OTHER, "Other"),
    )
    
    LANGUAGE_ENGLISH = "english"
    LANGUAGE_KOREAN = "korea"
    
    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korea"),
    )
    
    CURRENCY_USD = 'usd'
    CURRENCY_KRW = 'krw'
    
    CURRENCY_CHOICES = (
        (CURRENCY_USD, "Usd"),
        (CURRENCY_KRW, "Krw"),
    )
    
    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True, blank=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=2, null=True, blank=True)
    superhost = models.BooleanField(default=False)