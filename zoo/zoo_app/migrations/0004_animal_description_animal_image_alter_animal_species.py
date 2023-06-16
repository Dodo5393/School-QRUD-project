# Generated by Django 4.2.2 on 2023-06-13 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo_app', '0003_delete_animalcategory_alter_positions_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='animal',
            name='image',
            field=models.ImageField(default='', upload_to='animal_images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='animal',
            name='species',
            field=models.CharField(choices=[('mammal', 'Mammal'), ('bird', 'Bird'), ('reptile', 'Reptile'), ('amphibian', 'Amphibian'), ('fish', 'Fish')], max_length=100),
        ),
    ]
