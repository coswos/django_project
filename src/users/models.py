from django.db import models


# User(email, first_name, last_name, role_id)
class User(models.Model):
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.IntegerField()


# Role(value)
class Role(models.Model):
    value = models.CharField(max_length=15)


# Issue(title, body, timestamp, junior_id, senior_id, status)


# Message(body, issue_id, user_id)
class Message(models.Model):
    body = models.CharField(max_length=255)
    issue_id = models.IntegerField()
    user_id = models.IntegerField()
