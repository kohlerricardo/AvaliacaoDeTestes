def calcular_situacao_aluno(nota1, nota2, nota3):
    if nota1 < 0 or nota2 < 0 or nota3 < 0:
        raise ValueError("Notas não podem ser negativas.")

    media = (nota1 * 2 + nota2 * 7 + nota3 * 5) / 14
    # Ajustado divisor para a soma dos pesos (14)

    if media > 7.0:
        return "Aprovado"

    elif media > 5.0 and media <= 6.9:
        return "Recuperação"
    else:
        return "Reprovado"
    
resultado1 = calcular_situacao_aluno(8.0, 7.0, 9.0)
print(f"Teste 1 (Esperado: Aprovado) -> Resultado: {resultado1}")

resultado2 = calcular_situacao_aluno(5.0, 6.0, 5.0)
print(f"Teste 2 (Esperado: Recuperação) -> Resultado: {resultado2}")

resultado3 = calcular_situacao_aluno(2.0, 3.0, 1.0)
print(f"Teste 3 (Esperado: Reprovado) -> Resultado: {resultado3}")