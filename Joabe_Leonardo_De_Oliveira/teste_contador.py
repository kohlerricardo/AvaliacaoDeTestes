from contador_de_letras import contar_letras

def testar_contador():
    
    resultado = contar_letras ("amor")
    assert resultado == {"vogais": 2, "consoantes": 2}, f"Resultado esperado vogais: 2, consoantes: 2, resultado recebido {resultado}"

testar_contador()

def testar_aplha():

    resultado = contar_letras("senha 123")
    assert resultado == {"vogais":2, "consoantes":3}, f"resultado esperado vogais:2, consoantes: 3, resultado recebido{resultado}"

testar_aplha()


def testar_maiusculo():
    resultado = contar_letras("ALUNO")
    assert resultado == {"vogais":3, "consoantes":2}, f"resultado esperado vogais:3, consoantes:2, resultado recebido{resultado}"

testar_maiusculo()


def testar_sem_texto():
    resultado = contar_letras("")
    assert resultado == {"vogais":0, "consoantes":0}, f"resultado esperado vogais:0, consoantes:0, resultado recebido{resultado}"

testar_sem_texto()
