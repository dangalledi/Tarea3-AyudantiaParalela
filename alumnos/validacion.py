from rest_framework import serializers

def valor_nota(nota):#validacion de notas
    if nota <= 0 or nota > 7:
        raise serializers.ValidationError("NOTA NO VALIDA")
