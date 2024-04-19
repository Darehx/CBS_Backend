from rest_framework import serializers
from .models import workshops
from django.contrib.auth.models import User


class wpSerializer(serializers.ModelSerializer):
    fecha_wp = serializers.DateField()

    class Meta:
        model = workshops
        fields = ('id', 'nombre', 'apellido', 'dni', 'fecha_wp',
                  'workshop', 'instructor', 'codigo')


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'email', 'password']  # Puedes ajustar los campos aquí



