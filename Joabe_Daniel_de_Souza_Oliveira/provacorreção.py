def calcular_situacao_aluno(nota1, nota2, nota3):
    if not (0 <= nota1 <= 10 and
            0 <= nota2 <= 10 and
            0 <= nota3 <= 10):
        raise ValueError("As notas devem estar entre 0 e 10.")

    media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10

    if media >= 7.0:
        return media, "Aprovado"
    elif media >= 5.0:
        return media, "Recuperação"
    else:
        return media, "Reprovado"


try:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media, situacao = calcular_situacao_aluno(nota1, nota2, nota3)

    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")

except ValueError as erro:
    print(f"Erro: {erro}")
    notafinal = 0.0