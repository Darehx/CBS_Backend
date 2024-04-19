# Generated by Django 5.0.3 on 2024-03-16 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('password', models.CharField(max_length=200)),
                ('rol', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='workshops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre completo')),
                ('apellido', models.CharField(max_length=200, verbose_name='Apellidos')),
                ('dni', models.CharField(max_length=200)),
                ('fecha_wp', models.DateField(blank=True, null=True)),
                ('workshop', models.CharField(blank=True, default=' ', max_length=200)),
                ('instructor', models.CharField(blank=True, max_length=200, null=True)),
                ('codigo', models.CharField(default='9400-PM', max_length=200, unique=True)),
            ],
        ),
    ]