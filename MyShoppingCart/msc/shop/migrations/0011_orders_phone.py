# Generated by Django 4.0.5 on 2022-07-02 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=111),
        ),
    ]