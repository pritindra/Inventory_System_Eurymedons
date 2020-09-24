from django.contrib.auth.models import User
from users.models import UserInfo
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = UserInfo
        fields = ['user', 'designation', 'email', 'phone_number', 'branch_addr' ]