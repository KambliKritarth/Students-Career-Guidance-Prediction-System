# Generated by Django 3.2.5 on 2021-09-22 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0002_post_title_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dbf_score', models.IntegerField()),
            ],
        ),
    ]
