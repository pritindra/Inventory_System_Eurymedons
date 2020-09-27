from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ItemObject(models.Model):
    # Static Variables
    AVAILABLE = 1
    CHECKED_OUT = 2
    STATUS_CHOICES = (
        (AVAILABLE, 'Available'),
        (CHECKED_OUT, 'Checked Out'),
    )

    # Fields
    slug             = models.SlugField(unique=True)
    date_added       = models.DateField(auto_now_add=True)
    last_checkin     = models.DateTimeField(editable=False, null=True)
    status = models.PositiveIntegerField(choices=STATUS_CHOICES, default=AVAILABLE)
    who_has          = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    times_out        = models.PositiveIntegerField(default=0, editable=False)
    notes            = models.CharField(blank=True, max_length=500)
    history = models.ManyToManyField(User, through='ItemHistory', related_name='item_history', blank=True)
    

    def _last_checkout(self):
        try:
            return self.history.filter(activity=ItemHistory.CHECKED_OUT)[0].timestamp
        except IndexError:
            return None
    last_checkout = property(_last_checkout)

    def _last_activity(self):
        try:
            return self.history.all()[0].timestamp
        except IndexError:
            return None
    last_activity = property(_last_activity)

class ItemHistory(models.Model):
    CHECKED_OUT = 1
    RETURNED = 2
    ACTIVITY_CHOICES = (
        (CHECKED_OUT, 'Checked Out'),
        (RETURNED, 'Returned'),
    )

    item = models.ForeignKey(ItemObject, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.PositiveIntegerField(choices=ACTIVITY_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp'] # latest first