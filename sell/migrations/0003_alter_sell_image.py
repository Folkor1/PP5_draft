# Generated by Django 3.2 on 2023-01-16 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0002_auto_20230116_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
