from django.db import models                    #creating models
import datetime                                 #for adding datetime functionality
from threading import local
import pytz
from django.contrib.auth.models import User     #for adding login functionality
from django.urls import reverse
from django.utils import timezone

class Todo(models.Model):              #Our todolist model
    text = models.CharField(max_length=200)
    priority = models.CharField(max_length=8, default="", editable=True)
    type = models.CharField(max_length=20,default="", editable=True)
    duedate = models.DateTimeField(default=timezone.now, blank=False,editable=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    #def get_absolute_url(self):
    #        return reverse('user-todos' ,kwargs ={'username': self.author.username})
