from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Trips(models.Model):
    title = models.TextField()
    agent = models.TextField()
    image = models.TextField()
    popularity = models.TextField()

    class Meta:
        db_table = 'trips'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey('Trips', on_delete=models.CASCADE)
    comment = models.TextField()

    class Meta:
        db_table = 'comments'


class Agents(models.Model):
    title = models.TextField()
    url = models.TextField()
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'agents'


class AgencyRequests(models.Model):
    title = models.TextField()
    url = models.TextField()
    phone_number = models.CharField(max_length=20, null=False, blank=True)

    class Meta:
        db_table = 'agency_requests'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default_avatar.png')

    def __str__(self):
        return self.user.username
