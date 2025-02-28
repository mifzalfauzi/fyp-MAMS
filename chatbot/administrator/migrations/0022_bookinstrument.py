# Generated by Django 5.0.2 on 2024-05-12 02:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0021_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInstrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.book')),
                ('instrumentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.instrument')),
            ],
        ),
    ]
