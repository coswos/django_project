from django.db import models
from shared.django import TimestampMixin


# Create your models here.
class Issue(TimestampMixin):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=255)
    status = models.CharField(max_length=10)

    junior_id = models.IntegerField()
    senior_id = models.IntegerField(null=True)

    class Meta:
        db_table = "issues"


# Message(body, issue_id, user_id)
class Message(TimestampMixin):
    content = models.CharField(max_length=255)

    author_id = models.IntegerField()
    issue_id = models.IntegerField()

    class Meta:
        db_table = "issues/messages"
