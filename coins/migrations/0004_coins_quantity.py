# Generated by Django 3.2 on 2023-01-09 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0003_alter_coins_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='coins',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]