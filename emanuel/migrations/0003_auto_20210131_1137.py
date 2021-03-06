# Generated by Django 2.2.17 on 2021-01-31 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emanuel', '0002_auto_20210130_1828'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gabarito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('nome_materia', models.CharField(max_length=55, unique=True, verbose_name='Disciplina')),
                ('questao_1', models.CharField(max_length=100, verbose_name='Questão 1')),
                ('opcao_1_1', models.CharField(max_length=100, verbose_name='a')),
                ('opcao_1_2', models.CharField(max_length=100, verbose_name='b')),
                ('opcao_1_3', models.CharField(max_length=100, verbose_name='c')),
                ('resposta_da_questao_1', models.CharField(max_length=1, verbose_name='resposta')),
                ('peso_da_questao_1', models.IntegerField(default=1)),
                ('questao_2', models.CharField(max_length=100, verbose_name='Questão 2')),
                ('opcao_2_1', models.CharField(max_length=100, verbose_name='a')),
                ('opcao_2_2', models.CharField(max_length=100, verbose_name='b')),
                ('opcao_2_3', models.CharField(max_length=100, verbose_name='c')),
                ('resposta_da_questao_2', models.CharField(max_length=1, verbose_name='resposta')),
                ('peso_da_questao_2', models.IntegerField(default=3)),
                ('questao_3', models.CharField(max_length=100, verbose_name='Questão 3')),
                ('opcao_3_1', models.CharField(max_length=100, verbose_name='a')),
                ('opcao_3_2', models.CharField(max_length=100, verbose_name='b')),
                ('opcao_3_3', models.CharField(max_length=100, verbose_name='c')),
                ('resposta_da_questao_3', models.CharField(max_length=1, verbose_name='resposta')),
                ('peso_da_questao_3', models.IntegerField(default=4)),
                ('questao_4', models.CharField(max_length=100, verbose_name='Questão 4')),
                ('opcao_4_1', models.CharField(max_length=100, verbose_name='a')),
                ('opcao_4_2', models.CharField(max_length=100, verbose_name='b')),
                ('opcao_4_3', models.CharField(max_length=100, verbose_name='c')),
                ('resposta_da_questao_4', models.CharField(max_length=1, verbose_name='resposta')),
                ('peso_da_questao_4', models.IntegerField(default=2)),
            ],
            options={
                'verbose_name': 'gabarito',
                'verbose_name_plural': 'gabaritos',
            },
        ),
        migrations.CreateModel(
            name='Prova',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('resposta_do_aluno_questao_1', models.CharField(max_length=1, verbose_name='Resposta 1ª')),
                ('resposta_do_aluno_questao_2', models.CharField(max_length=1, verbose_name='Resposta 2ª')),
                ('resposta_do_aluno_questao_3', models.CharField(max_length=1, verbose_name='Resposta 3ª')),
                ('resposta_do_aluno_questao_4', models.CharField(max_length=1, verbose_name='Resposta 4ª')),
            ],
            options={
                'verbose_name': 'prova',
                'verbose_name_plural': 'provas',
            },
        ),
        migrations.CreateModel(
            name='Situacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('aluno', models.CharField(max_length=55)),
                ('nome_da_materia', models.CharField(max_length=55)),
                ('nota_da_prova_1', models.DecimalField(decimal_places=True, max_digits=2)),
                ('nota_da_prova_2', models.DecimalField(decimal_places=True, max_digits=2)),
                ('nota_da_prova_3', models.DecimalField(decimal_places=True, max_digits=2)),
                ('nota_da_prova_4', models.DecimalField(decimal_places=True, max_digits=2)),
                ('media_final', models.DecimalField(decimal_places=True, max_digits=2)),
                ('situacao', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'situacao',
                'verbose_name_plural': 'situacoes',
            },
        ),
        migrations.RemoveField(
            model_name='provaaluno',
            name='aluno',
        ),
        migrations.RemoveField(
            model_name='provaaluno',
            name='prova',
        ),
        migrations.DeleteModel(
            name='Sit',
        ),
        migrations.RenameField(
            model_name='aluno',
            old_name='nome_do_aluno',
            new_name='aluno',
        ),
        migrations.DeleteModel(
            name='Gab',
        ),
        migrations.DeleteModel(
            name='ProvaAluno',
        ),
        migrations.AddField(
            model_name='prova',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provas', to='emanuel.Aluno'),
        ),
        migrations.AddField(
            model_name='prova',
            name='provas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gabaritos', to='emanuel.Gabarito'),
        ),
    ]
