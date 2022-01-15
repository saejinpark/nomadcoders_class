from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    """ Custon User Model """
    
    PREFERENCE_BOOKS = "books"
    PREFERENCE_MOVIES = "movies"
    
    PREFERENCE_CHOICES = (
        (PREFERENCE_BOOKS, "Books"),
        (PREFERENCE_MOVIES, "Movies"),
    )
    
    LANGUAGE_ENGLISH = "english"
    LANGUAGE_KOREAN = "korea"
    
    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korea"),
    )
    
    bio = models.TextField(default="")
    Preference = models.CharField(choices=PREFERENCE_CHOICES, max_length=10, null=True, blank=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=10, null=True, blank=True)
    favourite_Book_Genre = models.CharField(max_length=10, null=True, blank=True)
    favourite_Movie_Genre = models.CharField(max_length=10, null=True, blank=True)