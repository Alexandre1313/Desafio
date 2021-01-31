from django.db import models


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Aluno(Base):
    matricula_do_aluno = models.IntegerField(unique=True)
    aluno = models.CharField(max_length=55)

    class Meta:
        verbose_name = 'aluno'
        verbose_name_plural = 'alunos'

    def __str__(self):
        return self.aluno


class Gabarito(Base):
    nome_materia = models.CharField('Disciplina', max_length=55, unique=True)
    questao_1 = models.CharField('Questão 1', max_length=100)
    opcao_1_1 = models.CharField('a', max_length=100)
    opcao_1_2 = models.CharField('b', max_length=100)
    opcao_1_3 = models.CharField('c', max_length=100)
    resposta_da_questao_1 = models.CharField('resposta', max_length=1)
    peso_da_questao_1 = models.IntegerField(default=1)
    questao_2 = models.CharField('Questão 2', max_length=100)
    opcao_2_1 = models.CharField('a', max_length=100)
    opcao_2_2 = models.CharField('b', max_length=100)
    opcao_2_3 = models.CharField('c', max_length=100)
    resposta_da_questao_2 = models.CharField('resposta', max_length=1)
    peso_da_questao_2 = models.IntegerField(default=3)
    questao_3 = models.CharField('Questão 3', max_length=100)
    opcao_3_1 = models.CharField('a', max_length=100)
    opcao_3_2 = models.CharField('b', max_length=100)
    opcao_3_3 = models.CharField('c', max_length=100)
    resposta_da_questao_3 = models.CharField('resposta', max_length=1)
    peso_da_questao_3 = models.IntegerField(default=4)
    questao_4 = models.CharField('Questão 4', max_length=100)
    opcao_4_1 = models.CharField('a', max_length=100)
    opcao_4_2 = models.CharField('b', max_length=100)
    opcao_4_3 = models.CharField('c', max_length=100)
    resposta_da_questao_4 = models.CharField('resposta', max_length=1)
    peso_da_questao_4 = models.IntegerField(default=2)

    class Meta:
        verbose_name = 'gabarito'
        verbose_name_plural = 'gabaritos'

    def __str__(self):
        return self.nome_materia


class Prova(Base):
    aluno = models.ForeignKey(Aluno, related_name='provas', on_delete=models.CASCADE)
    provas = models.ForeignKey(Gabarito, related_name='gabaritos', on_delete=models.CASCADE)
    resposta_do_aluno_questao_1 = models.CharField('Resposta 1ª', max_length=1)
    resposta_do_aluno_questao_2 = models.CharField('Resposta 2ª', max_length=1)
    resposta_do_aluno_questao_3 = models.CharField('Resposta 3ª', max_length=1)
    resposta_do_aluno_questao_4 = models.CharField('Resposta 4ª', max_length=1)

    class Meta:
        verbose_name = 'prova'
        verbose_name_plural = 'provas'

    def __str__(self):
        return self.aluno


class Situacao(Base):
    aluno = models.CharField(max_length=55)
    nome_da_materia = models.CharField(max_length=55)
    nota_da_prova_1 = models.DecimalField(max_digits=2, decimal_places=True)
    nota_da_prova_2 = models.DecimalField(max_digits=2, decimal_places=True)
    nota_da_prova_3 = models.DecimalField(max_digits=2, decimal_places=True)
    nota_da_prova_4 = models.DecimalField(max_digits=2, decimal_places=True)
    media_final = models.DecimalField(max_digits=2, decimal_places=True)
    situacao = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'situacao'
        verbose_name_plural = 'situacoes'

    def __str__(self):
        return self.aluno
