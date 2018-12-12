from rest_framework.viewsets import ModelViewSet

from enderecos.models import Endereco
from .serializers import EnderecoSerializer


class EnderecoViewset(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
