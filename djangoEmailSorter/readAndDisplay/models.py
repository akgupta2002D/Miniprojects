from django.db import models


class Email(models.Model):
    subject = models.CharField(max_length=255)
    received_time = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.subject
