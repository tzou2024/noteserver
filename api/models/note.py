
from django.db import models
from django.contrib.auth import get_user_model
from .folder import Folder

# Create your models here.
class Note(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  title = models.TextField(null=True, blank=True, default="unnamed note")
  body = models.TextField(null=True, blank=True)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)
  folder = models.ForeignKey(
    Folder, related_name='notes', on_delete=models.CASCADE
  )
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )
  def __str__(self):
        return self.body[0:50]

  def as_dict(self):
    """Returns dictionary version of Mango models"""
    return {
        'id': self.id,
        'body': self.body
    }
