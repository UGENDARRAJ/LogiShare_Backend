# Generated by Django 5.0 on 2024-05-17 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datas',
            name='Address',
        ),
        migrations.RemoveField(
            model_name='datas',
            name='Age',
        ),
        migrations.RemoveField(
            model_name='datas',
            name='Contact',
        ),
        migrations.RemoveField(
            model_name='datas',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='datas',
            name='Name',
        ),
        migrations.AddField(
            model_name='datas',
            name='Drop',
            field=models.CharField(default='Drop', max_length=20),
        ),
        migrations.AddField(
            model_name='datas',
            name='Height',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='datas',
            name='Length',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='datas',
            name='Pickup',
            field=models.CharField(default='Pick', max_length=20),
        ),
        migrations.AddField(
            model_name='datas',
            name='Quantity',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='datas',
            name='Type',
            field=models.CharField(default='MiniTruck', max_length=20),
        ),
        migrations.AddField(
            model_name='datas',
            name='Weight',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='datas',
            name='Width',
            field=models.IntegerField(default='0'),
        ),
    ]
