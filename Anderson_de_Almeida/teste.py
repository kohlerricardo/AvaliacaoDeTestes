from calculo_media import calcular_situacao_aluno

print("Rodando testes...\n")

resultado = calcular_situacao_aluno(8.0, 8.0, 8.0)
assert resultado == "Aprovado"
print("CT01 - Passou")

resultado = calcular_situacao_aluno(5.0, 6.0, 6.0)
assert resultado == "Recuperação"
print("CT02 - Passou")

resultado = calcular_situacao_aluno(4.0, 3.0, 4.0)
assert resultado == "Reprovado"
print("CT03 - Passou")

resultado = calcular_situacao_aluno(7.0, 7.0, 7.0)
assert resultado == "Aprovado"
print("CT04 - Passou")

resultado = calcular_situacao_aluno(5.0, 5.0, 5.0)
assert resultado == "Recuperação"
print("CT05 - Passou")

try:
    calcular_situacao_aluno(-2.0, 5.0, 8.0)
    print("CT06 - Falhou")
except ValueError:
    print("CT06 - Passou")

print("\nTodos os testes passaram!")