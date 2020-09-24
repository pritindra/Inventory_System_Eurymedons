from django.contrib import admin
from users.models import UserInfo, Activity


# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Activity)
