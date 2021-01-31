from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Gabarito, Prova, Aluno, Situacao
from .serializers import GabaritoSerializer, ProvaSerializer,\
    AlunoSerializer, SituacaoSerializer

# API v1


class GabaritosAPIView(generics.ListCreateAPIView):
    queryset = Gabarito.objects.all()
    serializer_class = GabaritoSerializer


class GabaritoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gabarito.objects.all()
    serializer_class = GabaritoSerializer


class ProvasAPIView(generics.ListCreateAPIView):
    queryset = Prova.objects.all()
    serializer_class = ProvaSerializer


class ProvaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prova.objects.all()
    serializer_class = ProvaSerializer


class AlunosAPIView(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class AlunoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class SituacoesAPIView(generics.ListCreateAPIView):
    queryset = Situacao.objects.all()
    serializer_class = SituacaoSerializer


class SituacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Situacao.objects.all()
    serializer_class = SituacaoSerializer

# API v2


class GabaritosViewSet(viewsets.ModelViewSet):
    queryset = Gabarito.objects.all()
    serializer_class = GabaritoSerializer


class ProvasViewSet(viewsets.ModelViewSet):
    queryset = Prova.objects.all()
    serializer_class = ProvaSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    @action(detail=True, methods=['Get'])
    def provas(self, request, pk=None):
        aluno = self.get_object()
        serializer = ProvaSerializer(aluno.provas.all(), many=True)
        return Response(serializer.data)


class SituacoesViewSet(viewsets.ModelViewSet):
    queryset = Situacao.objects.all()
    serializer_class = SituacaoSerializer
