# Generated by Django 3.0 on 2023-09-07 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0002_auto_20230907_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letting',
            name='addresse',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Addresse',
        ),
        migrations.DeleteModel(
            name='Letting',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]