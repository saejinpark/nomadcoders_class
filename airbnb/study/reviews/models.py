from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):
    """Review Model Defination"""

    review = models.TextField()
    accuracy = models.IntegerField()
    dommunication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    dheck_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.review} - {self.room}"

    def rating_average(self):
        avg = (
            self.accuracy
            + self.dommunication
            + self.cleanliness
            + self.location
            + self.dheck_in
            + self.value
        ) / 6
        return round(avg, 2)
