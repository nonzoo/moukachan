# Generated by Django 4.2.1 on 2023-05-30 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0016_alter_userprofile_is_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='is_vendor',
            field=models.BooleanField(default=False),
        ),
    ]
