from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone

from datetime import datetime

now = timezone.now


GIFT = (
        ('1','Image'),
        ('2', 'Video'),
        ('3', 'Quote'),
)

YEARS = (
    (2021, 2021),
    (2022, 2022),
    (2023, 2023),
    (2024, 2024),
    (2025, 2025),
)

class Calendar(models.Model): 
    """ 
    A unique calendar for each user, containing a unique id
    """
    user = models.ForeignKey(User, related_name='calendars', on_delete=models.CASCADE)
    unique_id = models.UUIDField(default=uuid.uuid4, max_length=100, unique=True, primary_key=True)
    name = models.CharField(max_length=254)
    days = models.IntegerField(default=0, choices=[(24, 24 ), (25, 25)])
    year = models.IntegerField(default=2021, choices=YEARS)
    is_public = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name


class Date(models.Model):
    
    class Meta:
        verbose_name_plural = 'Calendar Dates'

    calendar = models.ForeignKey(Calendar, related_name='dates',
                                 on_delete=models.CASCADE)
    gift = models.CharField(max_length=254, choices=GIFT, default='1')
    date = models.IntegerField()
    content = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Dates'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.date.strftime('%d %b %Y')
    
    def can_be_opened(self):
        date = datetime(year=self.calendar.year, month=12, day=self.date)
        if date <= datetime.now():
            return True
        return False

