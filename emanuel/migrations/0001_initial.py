# Generated by Django 2.2.17 on 2021-01-29 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('matricula_do_aluno', models.IntegerField(unique=True)),
                ('nome_do_aluno', models.CharField(max_length=55)),
            ],
            options={
                'verbose_name': 'aluno',
                'verbose_name_plural': 'alunos',
            },
        ),
        migrations.CreateModel(
            name='Gab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('nome_materia', models.CharField(max_length=55, unique=True)),
                ('questao_1', models.CharField(max_length=100)),
                ('opcao_1_1', models.CharField(max_length=100)),
                ('opcao_1_2', models.CharField(max_length=100)),
                ('opcao_1_3', models.CharField(max_length=100)),
                ('resposta_da_questao_1', models.CharField(max_length=1)),
                ('peso_da_questao_1', models.IntegerField(default=1)),
                ('questao_2', models.CharField(max_length=100)),
                ('opcao_2_1', models.CharField(max_length=100)),
                ('opcao_2_2', models.CharField(max_length=100)),
                ('opcao_2_3', models.CharField(max_length=100)),
                ('resposta_da_questao_2', models.CharField(max_length=1)),
                ('peso_da_questao_2', models.IntegerField(default=3)),
                ('questao_3', models.CharField(max_length=100)),
                ('opcao_3_1', models.CharField(max_length=100)),
                ('opcao_3_2', models.CharField(max_length=100)),
                ('opcao_3_3', models.CharField(max_length=100)),
                ('resposta_da_questao_3', models.CharField(max_length=1)),
                ('peso_da_questao_3', models.IntegerField(default=4)),
                ('questao_4', models.CharField(max_length=100)),
                ('opcao_4_1', models.CharField(max_length=100)),
                ('opcao_4_2', models.CharField(max_length=100)),
                ('opcao_4_3', models.CharField(max_length=100)),
                ('resposta_da_questao_4', models.CharField(max_length=1)),
                ('peso_da_questao_4', models.IntegerField(default=2)),
            ],
            options={
                'verbose_name': 'gabarito',
                'verbose_name_plural': 'gabaritos',
            },
        ),
        migrations.CreateModel(
            name='Sit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('nome_do_aluno', models.CharField(max_length=55)),
                ('nome_da_materia', models.CharField(max_length=55)),
                ('nota_da_prova_1', models.DecimalField(decimal_places=True, max_digits=2)),
                ('nota_da_prova_2', models.DecimalField(decimal_places=True, max_digits=2)),
                ('nota_da_prova_3', models.DecimalField(decimal_places=True, max_digits=2)),
                ('nota_da_prova_4', models.DecimalField(decimal_places=True, max_digits=2)),
                ('media_final', models.DecimalField(decimal_places=True, max_digits=2)),
                ('situacao', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Situacao',
                'verbose_name_plural': 'Situacoes',
            },
        ),
        migrations.CreateModel(
            name='ProvaAluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('resposta_do_aluno_questao_1', models.CharField(max_length=1)),
                ('resposta_do_aluno_questao_2', models.CharField(max_length=1)),
                ('resposta_do_aluno_questao_3', models.CharField(max_length=1)),
                ('resposta_do_aluno_questao_4', models.CharField(max_length=1)),
                ('nome_do_aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Provas',
                                                    to='emanuel.Aluno')),
                ('nome_materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Matérias',
                                                   to='emanuel.Gab')),
            ],
            options={
                'verbose_name': 'resposta',
                'verbose_name_plural': 'respostas',
            },
        ),
    ]
