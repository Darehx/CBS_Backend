# Generated by Django 5.0.3 on 2024-03-16 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0002_alter_workshops_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshops',
            name='codigo',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
