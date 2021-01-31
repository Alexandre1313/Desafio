from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import GabAPIView, ProvaAlunoAPIView, \
    AlunoAPIView, GabsAPIView, ProvasAlunoAPIView, AlunosAPIView, \
    SitAPIView, SitsAPIView, GabaritoViewSet, ProvaViewSet, AlunoViewSet, SituacaoViewSet

router = SimpleRouter()
router.register('gabarito', GabaritoViewSet)
router.register('prova', ProvaViewSet)
router.register('aluno', AlunoViewSet)
router.register('situacao', SituacaoViewSet)


urlpatterns = [
    path('gabaritos/', GabsAPIView.as_view(), name='gabaritos'),
    path('provas/', ProvasAlunoAPIView.as_view(), name='provas'),
    path('alunos/', AlunosAPIView.as_view(), name='alunos'),
    path('situacoes/', SitsAPIView.as_view(), name='situacoes'),
    path('gabaritos/<int:pk>/', GabAPIView.as_view(), name='gabarito'),
    path('provas/<int:pk>/', ProvaAlunoAPIView.as_view(), name='prova'),
    path('alunos/<int:pk>/', AlunoAPIView.as_view(), name='aluno'),
    path('situacoes/<int:pk>/', SitAPIView.as_view(), name='situacao'),
    ]
