from django.db import models


# Create your models here.
class Issue(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    junior_id = models.IntegerField()
    senior_id = models.IntegerField(null=True)
    status = models.CharField(max_length=10)
