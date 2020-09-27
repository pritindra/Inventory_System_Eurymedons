from django.db import models
from django.contrib.auth.models import User
from check.models import ItemObject
from PIL import Image

# Create your models here.
class Arsenal(models.Model):
    slug = models.OneToOneField(ItemObject,blank=True,null=True, on_delete=models.CASCADE)
    arsenal_type = models.CharField(max_length=20)
    arsenal_name = models.CharField(max_length=30, default='Gun')
    arsenal_number = models.IntegerField()
    arsenal_maintenance = models.BooleanField()
    arsenal_description = models.TextField(max_length=500,default='lorem ispum')
    arsenal_availability = models.TextField(max_length=1000)
    image = models.ImageField(default='default.jpg', upload_to='arsenal_pics')

class Vehicles(models.Model):
    slug = models.OneToOneField(ItemObject,blank=True,null=True, on_delete=models.CASCADE)    
    vehicle_type = models.CharField(max_length=20)
    vehicle_name = models.CharField(max_length=20, default='vehicle')
    vehicle_no = models.IntegerField()
    vehicle_description = models.TextField(max_length=500,default='lorem ispum')
    vehicle_availability = models.TextField(max_length=500)
    vehicle_maintenance = models.BooleanField()
    image = models.ImageField(default='default.jpg', upload_to='vehicles_pics')

class Criminal(models.Model):
    criminal_id = models.CharField(max_length=20)
    criminal_name = models.CharField(max_length=20)
    crime = models.CharField(max_length=30)
    crime_desc = models.TextField(max_length=200,null=True, blank=True)
    criminal_contact = models.TextField(max_length=200)
    arrest_date = models.DateTimeField()
    is_convict = models.BooleanField()
    image = models.ImageField(default='crime.jpg', upload_to='criminal_pics')
