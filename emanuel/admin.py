from django.contrib import admin
from .models import Gab, ProvaAluno, Aluno, Sit


@admin.register(Gab)
class GabAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'nome_materia',
                    'questao_1', 'opcao_1_1', 'opcao_1_2', 'opcao_1_3', 'resposta_da_questao_1',
                    'peso_da_questao_1',
                    'questao_2', 'opcao_2_1', 'opcao_2_2', 'opcao_2_3', 'resposta_da_questao_2',
                    'peso_da_questao_2',
                    'questao_3', 'opcao_3_1', 'opcao_3_2', 'opcao_3_3', 'resposta_da_questao_3',
                    'peso_da_questao_3',
                    'questao_4', 'opcao_4_1', 'opcao_4_2', 'opcao_4_3', 'resposta_da_questao_4',
                    'peso_da_questao_4',
                    'criacao')


@admin.register(ProvaAluno)
class ProvaAlunoAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'nome_do_aluno',
                    'nome_materia',
                    'resposta_do_aluno_questao_1',
                    'resposta_do_aluno_questao_2',
                    'resposta_do_aluno_questao_3',
                    'resposta_do_aluno_questao_4')


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'matricula_do_aluno', 'nome_do_aluno')


@admin.register(Sit)
class SitAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome_do_aluno', 'nome_da_materia',
        'nota_da_prova_1', 'nota_da_prova_2', 'nota_da_prova_3',
        'nota_da_prova_4', 'media_final', 'situacao'
    )