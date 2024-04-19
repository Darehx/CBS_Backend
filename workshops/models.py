# Create your models here.
from django.db import models

#Modelo para tabla/collection cursos/workshops
import random


class workshops(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre completo")  
    apellido = models.CharField(max_length=200, verbose_name="Apellidos") 
    dni = models.CharField(max_length=200) 
    fecha_wp = models.CharField(max_length=200, null=True,)
    workshop = models.CharField(max_length=200, blank=True, default=" ")
    instructor = models.CharField(max_length=200, null=True, blank=True)
    codigo = models.CharField(max_length=200, blank=True, unique=True) 
     # Agregamos el campo del código aquí
     
    def __str__(self):
        return self.nombre + ' Documento:' + self.dni + ' | Workshop Realizado:' + self.workshop

    def generar_codigo():
        # Genera cuatro dígitos aleatorios
        parte1 = str(random.randint(1000, 9999))
    
        # Genera dos letras aleatorias
        letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        parte2 = random.choice(letras) + random.choice(letras)
    
        # Combina las partes para formar el código
        codigo = parte1 + '-' + parte2
        return codigo

    @staticmethod
    def codigo_existe(codigo):
        # Consulta si el código ya existe en la base de datos
        return workshops.objects.filter(codigo=codigo).exists()

    def save(self, *args, **kwargs):
        # Antes de guardar, asegúrate de que el código sea único
        while True:
            certificado = workshops.generar_codigo()
            if not workshops.codigo_existe(certificado):
                self.codigo = certificado
                break
        super().save(*args, **kwargs)

   


class users(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.EmailField(max_length=254)
    password = models.CharField(max_length=200)
    rol = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre + '  | Access: ' + self.rol

