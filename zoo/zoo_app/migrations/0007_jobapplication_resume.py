# Generated by Django 4.2.2 on 2023-06-15 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo_app', '0006_jobapplication_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='resume',
            field=models.FileField(default='', upload_to='resumes/'),
            preserve_default=False,
        ),
    ]
