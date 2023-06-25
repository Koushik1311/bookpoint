from email.message import Message
from pyexpat import model
from django.db import models


class ContactModel(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    subject = models.CharField(max_length=255, null=False, blank=False)
    message = models.TextField(blank=False, null=False)
