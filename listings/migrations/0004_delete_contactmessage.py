# Generated by Django 5.0.6 on 2024-06-11 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_contactmessage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactMessage',
        ),
    ]
