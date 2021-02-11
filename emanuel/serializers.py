from rest_framework import serializers
# import requests
from .models import Gabarito, Prova, Aluno, Situacao


class Base1(serializers.ModelSerializer):
    pass


class GabaritoSerializerGab(Base1):
    class Meta:
        model = Gabarito
        fields = ('id', 'gabarito',
                  'resposta_da_questao_1',
                  'resposta_da_questao_2',
                  'resposta_da_questao_3',
                  'resposta_da_questao_4')


class GabaritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gabarito
        fields = ('id',
                  'gabarito',
                  'questao_1', 'opcao_1_1', 'opcao_1_2', 'opcao_1_3', 'resposta_da_questao_1',
                  # 'peso_da_questao_1',
                  'questao_2', 'opcao_2_1', 'opcao_2_2', 'opcao_2_3', 'resposta_da_questao_2',
                  # 'peso_da_questao_2',
                  'questao_3', 'opcao_3_1', 'opcao_3_2', 'opcao_3_3', 'resposta_da_questao_3',
                  # 'peso_da_questao_3',
                  'questao_4', 'opcao_4_1', 'opcao_4_2', 'opcao_4_3', 'resposta_da_questao_4',
                  # 'peso_da_questao_4',
                  'criacao')

    def validate_resposta_da_questao_1(self, valor):
        if valor in 'AaBbCc':
            return valor
        raise serializers.ValidationError('A resposta só pode ser A, B ou C')

    def validate_resposta_da_questao_2(self, valor):
        if valor in 'AaBbCc':
            return valor
        raise serializers.ValidationError('A resposta só pode ser A, B ou C')

    def validate_resposta_da_questao_3(self, valor):
        if valor in 'AaBbCc':
            return valor
        raise serializers.ValidationError('A resposta só pode ser A, B ou C')

    def validate_resposta_da_questao_4(self, valor):
        if valor in 'AaBbCc':
            return valor
        raise serializers.ValidationError('A resposta só pode ser A, B ou C')


class AlunoSerializer(serializers.ModelSerializer):
    provas = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='prova-detail')

    class Meta:
        model = Aluno
        fields = ('id',
                  'matricula_do_aluno',
                  'aluno', 'provas')


class ProvaSerializerGab(serializers.ModelSerializer):
    prova = GabaritoSerializerGab(read_only=True)

    class Meta:
        model = Prova
        fields = ('id',
                  'aluno',
                  'prova',
                  'resposta_do_aluno_questao_1',
                  'resposta_do_aluno_questao_2',
                  'resposta_do_aluno_questao_3',
                  'resposta_do_aluno_questao_4',
                  'prova')


class SituacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Situacao
        fields = (
            'id',
            'aluno',
            'curso',
            'media_final', 'situacao'
        )


class ProvaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prova
        fields = ('id',
                  'aluno',
                  'prova',
                  'resposta_do_aluno_questao_1',
                  'resposta_do_aluno_questao_2',
                  'resposta_do_aluno_questao_3',
                  'resposta_do_aluno_questao_4',
                  )

    def validate_resposta_do_aluno_questao_1(self, valor):
        if valor in 'AaBbCc':
            return valor
        raise serializers.ValidationError('A resposta só pode ser A, B ou C')

    def validate_resposta_do_aluno_questao_2(self, valor):
        if valor in 'AaBbCc':
            return valor
        raise serializers.ValidationError('A resposta só pode ser A, B ou C')

    def validate_resposta_do_aluno_questao_3(self, valor):
        if valor in 'AaBbCc':
            return valor
        raise serializers.ValidationError('A resposta só pode ser A, B ou C')

    def validate_resposta_do_aluno_questao_4(self, valor):
        if valor in 'AaBbCc':
            return valor
        raise serializers.ValidationError('A resposta só pode ser A, B ou C')
