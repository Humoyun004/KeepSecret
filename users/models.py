from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images', default='default_image.jpg')
    fullname = models.CharField(max_length=155)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=6, choices=[('Male', 'Male'), ('Female', 'Female')])

    def __str__(self):
        return self.user.username

