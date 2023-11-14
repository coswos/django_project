from django.db import models


# Create your models here.
class Issue(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    junior_id = models.IntegerField()
    senior_id = models.IntegerField(null=True)
    status = models.CharField(max_length=10)


# Role(value)
class Role(models.Model):
    value = models.CharField(max_length=15)


# Message(body, issue_id, user_id)
class Message(models.Model):
    body = models.CharField(max_length=255)
    issue_id = models.IntegerField()
    user_id = models.IntegerField()
