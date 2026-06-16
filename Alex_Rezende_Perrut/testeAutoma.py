from contador_de_letras import contar_letras

casos_teste = [
    ("teste", {"vogais": 2, "consoantes": 3}),
    ("ALUNO", {"vogais": 3, "consoantes": 2}),
    ("senha 123", {"vogais": 2, "consoantes": 3}),
    ("aeiou", {"vogais": 5, "consoantes": 0}),
    ("", {"vogais": 0, "consoantes": 0})
]

for entrada, esperado in casos_teste:
    resultado = contar_letras(entrada)
    assert resultado == esperado, f"Erro: {entrada} -> {resultado}, esperado {esperado}"

print("Todos os testes passaram!")