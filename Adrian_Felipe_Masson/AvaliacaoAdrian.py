
def calcular_situacao_aluno(nota1, nota2, nota3):
    
    media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / (2 + 3 + 5)

    if nota1 < 0 or nota2 < 0 or nota3 < 0:
        raise ValueError ("Notas não podem ser negativas.")

    if media >= 7.0:
        return "Aprovado"

    elif media >= 5.0 and media <= 6.9:
        return "Recuperação"
    else:
        return "Reprovado"