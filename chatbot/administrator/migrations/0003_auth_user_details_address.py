# Generated by Django 5.0.2 on 2024-04-07 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0002_rename_phonenumber_auth_user_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='auth_user_details',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
