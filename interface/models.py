from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Arsenal(models.Model):
    arsenal_type = models.CharField(max_length=20)
    arsenal_name = models.CharField(max_length=30)
    arsenal_number = models.IntegerField()
    arsenal_maintenance = models.BooleanField()
    arsenal_availability = models.TextField(max_length=1000)
    image = models.ImageField(default='default.jpg', upload_to='arsenal_pics')
