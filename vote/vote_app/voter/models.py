from django.db import models

class Voter(models.Model):
    name = models.CharField(max_length=100)
    voter_id = models.CharField(max_length=50, unique=True)
    dob = models.DateField()

    def __str__(self):
        return self.name
