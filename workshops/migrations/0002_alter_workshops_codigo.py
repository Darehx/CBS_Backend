# Generated by Django 5.0.3 on 2024-03-16 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshops',
            name='codigo',
            field=models.CharField(default='2872-NK', max_length=200, unique=True),
        ),
    ]
