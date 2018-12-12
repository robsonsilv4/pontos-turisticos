from django.db import models
from atracoes.models import Atracao
from enderecos.models import Endereco
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)

    def __str__(self):
        return self.nome
