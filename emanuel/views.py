from rest_framework import generics
from .models import Gab, ProvaAluno, Aluno, Sit
from .serializers import GabSerializer, ProvaAlunoSerializer,\
    AlunoSerializer, SitSerializer


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
