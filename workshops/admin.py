from django.contrib import admin
from .models import workshops, users

class WorkshopsAdmin(admin.ModelAdmin):
    # Personaliza las opciones del administrador si es necesario
    pass

admin.site.register(workshops, WorkshopsAdmin)
admin.site.register(users)  # Registra el modelo 'users' por separado
