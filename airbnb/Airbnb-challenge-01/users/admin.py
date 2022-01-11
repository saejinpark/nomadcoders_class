from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    
    """ Custom User Admin """
    
    fieldsets = UserAdmin.fieldsets + (("Banaan", {"fields": ("bio", "Preference", "language", "favourite_Book_Genre", "favourite_Movie_Genre" )}),)
    list_display = ("bio", "Preference", "language", "favourite_Book_Genre", "favourite_Movie_Genre" )
    list_filter = ("bio", "Preference", "language", "favourite_Book_Genre", "favourite_Movie_Genre" )