# Generated by Django 3.0.5 on 2020-04-25 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_movrotativo_now'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movrotativo',
            name='now',
        ),
    ]