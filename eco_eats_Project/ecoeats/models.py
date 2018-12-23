from django.db import models
from enum import auto


class Users(models.Model):
    uname = models.CharField(max_length=128, unique=True)
    passweord = models.CharField(max_length=128)
     
    def __unicode__(self):  
        return self.uname

class Feedback(models.Model):
    username = models.ForeignKey(Users, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=1000)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def __unicode__(self):      
        return self.feedback