# Generated by Django 4.2.1 on 2023-05-29 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0010_alter_customuser_is_user_alter_customuser_is_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_vendor',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]