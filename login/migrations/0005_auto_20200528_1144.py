# Generated by Django 3.0.4 on 2020-05-28 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
