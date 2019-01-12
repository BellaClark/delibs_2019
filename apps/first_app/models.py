from django.db import models

class Person(models.Model):
    name = models.CharField(max_length = 255)
    total_vote = models.IntegerField(default='0', editable=True)
    people_voted = models.IntegerField(default='0', editable=True)
    average_vote = models.IntegerField(default='0', editable=True)