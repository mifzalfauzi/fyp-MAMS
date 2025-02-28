# Generated by Django 5.0.2 on 2024-03-21 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0008_datasetentry_roles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='datasetentry',
            name='roles',
        ),
        migrations.AddField(
            model_name='datasetentry',
            name='roles',
            field=models.ManyToManyField(to='assistant.role'),
        ),
    ]
