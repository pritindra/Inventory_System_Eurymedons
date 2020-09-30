from django.contrib import admin
from .models import Questionaire, Questions, Responses

# Register your models here.
admin.site.register(Questions)
admin.site.register(Questionaire)
admin.site.register(Responses)
