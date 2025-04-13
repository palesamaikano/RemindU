from django.db import models

class Reminder(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    type = models.CharField(max_length=100, blank=True)  # To store reminder type if needed (in future)

class Class(models.Model):
    title = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()

class Todo(models.Model):
    task = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)

class Test(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()