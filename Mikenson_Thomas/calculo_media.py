def calcular_situacao_aluno(nota1, nota2, nota3):
    if nota1 < 0 or nota2 < 0 or nota3 < 0:
        raise ValueError("Notas não podem ser negativas.")
    if nota1 > 10 or nota2 > 10 or nota3 > 10:
        raise ValueError("Notas não podem ser maiores que 10.")

    media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10

    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0 and media <= 6.99:
        return "Recuperação"
    else:
        return "Reprovado"
