from django.db import models
from datetime import datetime

class Feature(models.Model):
    name = models.CharField(max_length=30)
    details = models.TextField()


    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Message(models.Model):
    value = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now, blank=True, null=True)
    user = models.CharField(max_length=1000)
    room = models.CharField(max_length=1000)

    def __str__(self):
        return self.room


class Student(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    description = models.TextField(blank=True)
    date_enrolled =  models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return self.name



