# Generated by Django 4.2.7 on 2024-04-23 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novauser', '0003_alter_customuser_managers_alter_customuser_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]
