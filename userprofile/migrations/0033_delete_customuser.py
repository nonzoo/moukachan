# Generated by Django 4.2.1 on 2023-06-12 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0032_userprofile_website'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]