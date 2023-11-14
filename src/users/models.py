from django.db import models


# User(email, first_name, last_name, role_id)
class User(models.Model):
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.IntegerField()
