from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, related_name='this_guy_forgets_stuff')
    note = models.CharField(max_length=280)
    created = models.DateTimeField(auto_now_add=True)
    PRIORIDAD = (
        ('1', 'Alta'),
        ('2', 'Media'),
        ('3', 'Baja'),
        )
    priority = models.CharField(choices=PRIORIDAD, default='Baja', max_length=5)
    has_alarm = models.BooleanField(default=False)
    father_note = models.ForeignKey('self', related_name='nota_padre', blank=True, null=True)
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    image = models.ImageField(null=False, blank=True)

class Reminder(models.Model):
    note = models.ForeignKey(Note)
    reminder_time =  models.DateTimeField()