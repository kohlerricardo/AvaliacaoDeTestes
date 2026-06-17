def calcular_situacao_aluno(nota1, nota2, nota3):
    if not (0 <= nota1 <= 10) or not (0 <= nota2 <= 10) or not (0 <= nota3 <= 10):
        raise ValueError("Notas devem estar entre 0 e 10")

    media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10

    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperação"
    else:
        return "Reprovado"
        