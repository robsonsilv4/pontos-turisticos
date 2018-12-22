from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    def list(self, request, *args, **kwargs):
        return Response({
            'a': 1,
            'b': 2,
            'c': 3
        })

    def create(self, request, *args, **kwargs):
        return Response({'ola': 'Robson'})

    def destroy(self, request, *args, **kwargs):
        pass

    def retrieve(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    def partial_update(self, request, *args, **kwargs):
        pass

    @action(methods=['get', 'post'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass
