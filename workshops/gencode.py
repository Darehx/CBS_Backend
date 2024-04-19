#Modelo para tabla/collection cursos/workshops
import random
from .models import workshops

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



