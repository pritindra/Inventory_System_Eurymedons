from django.contrib import admin
from check.models import ItemHistory, ItemObject

# Register your models here.
admin.site.register(ItemObject)
admin.site.register(ItemHistory)