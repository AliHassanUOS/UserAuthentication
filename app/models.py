from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    image = models.ImageField()