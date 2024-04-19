from rest_framework import routers
from django.urls import path
from .api import wpapiViewSet
from .views import login
router = routers.DefaultRouter()

router.register('api/workshops', wpapiViewSet, 'workshops')

urlpatterns = [
    # Definir manualmente la URL de autenticación
    path('auth/', login, name='login'),

]

# Agregar las URL generadas por el enrutador al urlpatterns
urlpatterns += router.urls
