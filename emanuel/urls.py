from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import GabaritoAPIView, ProvaAPIView, \
    AlunoAPIView, GabaritosAPIView, ProvasAPIView, AlunosAPIView, \
    SituacaoAPIView, SituacoesAPIView, GabaritosViewSet, ProvasViewSet, AlunosViewSet, SituacoesViewSet

router = SimpleRouter()
router.register('gabarito', GabaritosViewSet)
router.register('prova', ProvasViewSet)
router.register('aluno', AlunosViewSet)
router.register('situacao', SituacoesViewSet)


urlpatterns = [
    path('gabaritos/', GabaritosAPIView.as_view(), name='gabaritos'),
    path('provas/', ProvasAPIView.as_view(), name='provas'),
    path('alunos/', AlunosAPIView.as_view(), name='alunos'),
    path('situacoes/', SituacoesAPIView.as_view(), name='situacoes'),
    path('gabaritos/<int:pk>/', GabaritoAPIView.as_view(), name='gabarito'),
    path('provas/<int:pk>/', ProvaAPIView.as_view(), name='prova'),
    path('alunos/<int:pk>/', AlunoAPIView.as_view(), name='aluno'),
    path('situacoes/<int:pk>/', SituacaoAPIView.as_view(), name='situacao'),
    ]
