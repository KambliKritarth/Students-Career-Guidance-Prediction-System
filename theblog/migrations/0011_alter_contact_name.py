# Generated by Django 3.2.5 on 2021-10-19 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0010_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=10),
        ),
    ]
