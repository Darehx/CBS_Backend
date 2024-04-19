from rest_framework import viewsets, permissions
from .models import workshops
from .serializers import wpSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class wpapiViewSet(viewsets.ModelViewSet):
    queryset = workshops.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = wpSerializer

    from rest_framework.decorators import action


class wpapiViewSet(viewsets.ModelViewSet):
    queryset = workshops.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = wpSerializer

    @action(detail=False, methods=['get'], url_path='code=(?P<codigo>[^/.]+)')
    def get_by_code(self, request, codigo):
        try:
            workshop = workshops.objects.get(codigo=codigo)
            serializer = self.get_serializer(workshop)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except workshops.DoesNotExist:
            return Response({"error": "Workshop not found"}, status=status.HTTP_404_NOT_FOUND)
