def calcular_situacao_aluno(nota1, nota2, nota3):
    if nota1 < 0 or nota2 < 0 or nota3 < 0:
        raise ValueError("Notas não podem ser negativas.")

    media = (nota1 * 2 + nota2 + 3 + nota3 * 5) / 3

    if media >=7.0:
        return "Aprovado"
#retirei o media <=6,9 por que todas notas abaixo de 7 presisa de recuperação.
    elif media > 5.0:
        return "Recuperação"
    else:
        return "Reprovado"
    
