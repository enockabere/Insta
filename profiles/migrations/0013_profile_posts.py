# Generated by Django 3.2.7 on 2021-09-19 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_auto_20210917_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='posts',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='mypost', to='profiles.image'),
        ),
    ]
