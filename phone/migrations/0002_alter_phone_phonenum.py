# Generated by Django 3.2.7 on 2021-09-09 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='phonenum',
            field=models.CharField(max_length=50, verbose_name='PHONE'),
        ),
    ]
