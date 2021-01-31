from rest_framework import generics
from rest_framework import viewsets
from .models import Gab, ProvaAluno, Aluno, Sit
from .serializers import GabSerializer, ProvaAlunoSerializer,\
    AlunoSerializer, SitSerializer

# API v1


class GabsAPIView(generics.ListCreateAPIView):
    queryset = Gab.objects.all()
    serializer_class = GabSerializer


class GabAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gab.objects.all()
    serializer_class = GabSerializer


class ProvasAlunoAPIView(generics.ListCreateAPIView):
    queryset = ProvaAluno.objects.all()
    serializer_class = ProvaAlunoSerializer


class ProvaAlunoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProvaAluno.objects.all()
    serializer_class = ProvaAlunoSerializer


class AlunosAPIView(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class AlunoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class SitsAPIView(generics.ListCreateAPIView):
    queryset = Sit.objects.all()
    serializer_class = SitSerializer


class SitAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sit.objects.all()
    serializer_class = SitSerializer

# API v2


class GabaritoViewSet(viewsets.ModelViewSet):
    queryset = Gab.objects.all()
    serializer_class = GabSerializer


class ProvaViewSet(viewsets.ModelViewSet):
    queryset = ProvaAluno.objects.all()
    serializer_class = ProvaAlunoSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class SituacaoViewSet(viewsets.ModelViewSet):
    queryset = Sit.objects.all()
    serializer_class = SitSerializer
