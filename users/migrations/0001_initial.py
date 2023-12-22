# Generated by Django 5.0 on 2023-12-19 16:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(default='default_image.jpg', upload_to='profile_images')),
                ('fullname', models.CharField(max_length=155)),
                ('phone_number', models.CharField(max_length=15)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
