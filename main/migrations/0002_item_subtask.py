# Generated by Django 4.2.3 on 2023-07-15 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='subtask',
            field=models.BooleanField(blank=True, default=False),
            preserve_default=False,
        ),
    ]