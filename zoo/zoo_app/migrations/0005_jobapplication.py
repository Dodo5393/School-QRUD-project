# Generated by Django 4.2.2 on 2023-06-14 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo_app', '0004_animal_description_animal_image_alter_animal_species'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('cover_letter', models.TextField()),
            ],
        ),
    ]
