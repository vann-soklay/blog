from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    job = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True),
    country = models.CharField(max_length=100, blank=True),

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, **kwargs):
        super().save()
