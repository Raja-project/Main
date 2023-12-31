# Generated by Django 4.2.2 on 2023-09-29 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corpHotelApp', '0002_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='hdesc',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hdisc',
            field=models.IntegerField(default=0, max_length=2),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hfacl',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hname',
            field=models.CharField(default=' ', max_length=15),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hprice',
            field=models.IntegerField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hrate',
            field=models.IntegerField(default=0, max_length=2),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hrooms',
            field=models.IntegerField(default=0, max_length=3),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='hid',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
