# Generated by Django 5.0.3 on 2024-03-18 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0005_alter_workshops_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='correo',
            field=models.EmailField(max_length=254),
        ),
    ]
