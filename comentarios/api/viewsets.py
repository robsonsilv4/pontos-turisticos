from rest_framework.viewsets import ModelViewSet

from comentarios.models import Comentario
from .serializers import ComentarioSerializer


class ComentarioViewset(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
