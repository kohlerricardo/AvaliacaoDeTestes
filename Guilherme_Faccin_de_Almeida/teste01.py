from Avaliação import contar_letras

def teste_letras01():
    resultado = contar_letras('teste')
    assert resultado == {"vogais": 2, "consoantes": 3},f'{resultado}'
    resultado = contar_letras('ALUNO')
    assert resultado == {"vogais": 3, "consoantes": 2},f'{resultado}'
    resultado = contar_letras('senha 123')
    assert resultado == {"vogais": 2, "consoantes": 3},f'{resultado}'
    resultado = contar_letras('aeiou')
    assert resultado == {"vogais": 5, "consoantes": 0},f'{resultado}'
    resultado = contar_letras('')
    assert resultado == {"vogais": 0, "consoantes": 0},f'{resultado}'
teste_letras01()