# Generated by Django 3.2.7 on 2021-10-10 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='github_link',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='linkedin_link',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]