from django.db import models

class GuessingGame(models.Model):
    secret_number = models.IntegerField()
    attempts = models.IntegerField(default=0)
    max_attempts = models.IntegerField(default=3)