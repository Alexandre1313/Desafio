from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins
from .models import Gabarito, Prova, Aluno, Situacao
from .serializers import GabaritoSerializer, ProvaSerializerGab, \
    AlunoSerializer, SituacaoSerializer, ProvaSerializer


# API v1 versão 1


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


# API v2 versão 2


class GabaritosViewSet(viewsets.ModelViewSet):
    queryset = Gabarito.objects.all()
    serializer_class = GabaritoSerializer


class ProvasViewSet(viewsets.ModelViewSet):
    # permission_classes = (permissions.DjangoModelPermissions, )
    queryset = Prova.objects.all()
    serializer_class = ProvaSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    @action(detail=True, methods=['Get'])
    def provas(self, request, pk=None):
        self.pagination_class.page_size = 5
        provas = Prova.objects.filter(aluno_id=pk)
        page = self.paginate_queryset(provas)
        if page is not None:
            serializer = ProvaSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ProvaSerializer(provas, many=True)
        return Response(serializer.data)


class SituacoesViewSet(viewsets.ModelViewSet):
    queryset = Situacao.objects.all()
    serializer_class = SituacaoSerializer


class CadastroGab(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Gabarito.objects.all()
    serializer_class = GabaritoSerializer


class ProvasViewSetGab(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Prova.objects.all()
    serializer_class = ProvaSerializerGab
