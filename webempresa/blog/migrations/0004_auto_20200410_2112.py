# Generated by Django 3.0.5 on 2020-04-10 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200410_2047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='name',
            new_name='title',
        ),
    ]
