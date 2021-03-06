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
        ordering = 'id',

    def __str__(self):
        return self.aluno


class Gabarito(Base):
    gabarito = models.CharField('Disciplina', max_length=55, unique=True)
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
        ordering = 'id',

    def __str__(self):
        return self.gabarito


class Prova(Base):
    aluno = models.ForeignKey(Aluno, related_name='provas', on_delete=models.CASCADE)
    prova = models.ForeignKey(Gabarito, related_name='gabaritos', on_delete=models.CASCADE)
    resposta_do_aluno_questao_1 = models.CharField('Resposta 1ª', max_length=1)
    resposta_do_aluno_questao_2 = models.CharField('Resposta 2ª', max_length=1)
    resposta_do_aluno_questao_3 = models.CharField('Resposta 3ª', max_length=1)
    resposta_do_aluno_questao_4 = models.CharField('Resposta 4ª', max_length=1)

    class Meta:
        verbose_name = 'prova'
        verbose_name_plural = 'provas'
        ordering = 'aluno',

    def __str__(self):
        return self.aluno


class Situacao(Base):
    aluno = models.ForeignKey(Aluno, max_length=55, related_name='situacoes', on_delete=models.CASCADE)
    curso = models.CharField(blank=True, max_length=55)
    media_final = models.DecimalField(max_digits=2, decimal_places=True)
    situacao = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'situacao'
        verbose_name_plural = 'situacoes'
        ordering = 'id',

    def __str__(self):
        return self.aluno
