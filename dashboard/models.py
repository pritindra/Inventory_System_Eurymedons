from django.db import models
from django.contrib.auth.models import User
from interface.models import Arsenal

# Create your models here.

class Item(models.Model):
    name=models.OneToOneField(Arsenal,blank=True,null=True, on_delete=models.CASCADE)
    quantity=models.IntegerField()


    def __str__(self):
        return "{}-{}".format(self.name, self.quantity)