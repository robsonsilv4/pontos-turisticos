from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from atracoes.api.serializers import AtracaoSerializer
from core.models import PontoTuristico
from enderecos.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    enderecos = EnderecoSerializer()

    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = (
            'id', 'nome', 'descricao', 'descricao_completa', 'descricao_completa', 'aprovado', 'foto', 'atracoes',
            'comentarios', 'avaliacoes',
            'enderecos')

    def get_descricao_completa(self, obj):
        return f'{obj.nome} {obj.descricao}'
