# Generated by Django 3.2 on 2023-01-16 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sell',
            old_name='name',
            new_name='coin_name',
        ),
        migrations.AddField(
            model_name='sell',
            name='email',
            field=models.EmailField(max_length=70, null=True),
        ),
    ]
