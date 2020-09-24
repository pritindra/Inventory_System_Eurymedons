from django.db import models

# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length=220)
    quantity=models.IntegerField()


    def __str__(self):
        return "{}-{}".format(self.name, self.quantity)