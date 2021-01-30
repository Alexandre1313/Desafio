from django.urls import path
from .views import GabAPIView, ProvaAlunoAPIView, \
    AlunoAPIView, GabsAPIView, ProvasAlunoAPIView, AlunosAPIView, \
    SitAPIView, SitsAPIView

urlpatterns = [
    path('gab/', GabsAPIView.as_view(), name='Gabaritos'),
    path('provaaluno/', ProvasAlunoAPIView.as_view(), name='Respostas'),
    path('aluno/', AlunosAPIView.as_view(), name='Alunos'),
    path('sit/', SitsAPIView.as_view(), name='Situacoes'),
    path('gab/<int:pk>/', GabAPIView.as_view(), name='Gabarito'),
    path('provaaluno/<int:pk>/', ProvaAlunoAPIView.as_view(), name='Resposta'),
    path('aluno/<int:pk>/', AlunoAPIView.as_view(), name='Aluno'),
    path('sit/<int:pk>/', SitAPIView.as_view(), name='Situacao'),
    ]
