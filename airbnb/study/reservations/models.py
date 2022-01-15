from django.db import models
from core import models as core_models
# Create your models here.


class Reservation(core_models.TimeStampedModel):
    
    """ Reservation Model Definition """
    
    SATUS_PENDING = "pending"
    SATUS_CONFIRMED = "confirmed"
    SATUS_CANCELED = "canceled"
    
    STATUS_CHOICES = (
        (SATUS_PENDING, "pending"),
        (SATUS_CONFIRMED, "confirmed"),
        (SATUS_CANCELED, "canceled"),
    )
    
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=SATUS_PENDING
        )
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'{self.room} - {self.check_in}'