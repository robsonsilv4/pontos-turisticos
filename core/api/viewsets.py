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

    # def destroy(self, request, *args, **kwargs):
    #     pass
