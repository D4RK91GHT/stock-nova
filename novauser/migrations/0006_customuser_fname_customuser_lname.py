# Generated by Django 4.2.7 on 2024-06-04 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novauser', '0005_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='fname',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='customuser',
            name='lname',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
