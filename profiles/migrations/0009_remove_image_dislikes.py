# Generated by Django 3.2.7 on 2021-09-16 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='dislikes',
        ),
    ]