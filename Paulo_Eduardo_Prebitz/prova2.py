from Prova import contar_letras


# TESTE 1: palavra simples
# Justificativa: valida funcionamento básico da função

def test_palavra_simples():
    assert contar_letras("banana") == {"vogais": 3, "consoantes": 3}



# TESTE 2: mistura de maiúsculas e minúsculas
# Justificativa: garante que .lower() funciona corretamente

def test_maiusculas():
    assert contar_letras("Abacaxi") == {"vogais": 4, "consoantes": 3}



# TESTE 3: apenas vogais
# Justificativa: valida caso extremo sem consoantes

def test_apenas_vogais():
    assert contar_letras("AEIOU") == {"vogais": 5, "consoantes": 0}



# TESTE 4: números e símbolos
# Justificativa: garante que caracteres não alfabéticos são ignorados

def test_numeros_e_simbolos():
    assert contar_letras("a1 b!") == {"vogais": 1, "consoantes": 1}



# TESTE 5: string vazia
# Justificativa: valida comportamento em entrada vazia (caso limite)

def test_vazio():
    assert contar_letras("") == {"vogais": 0, "consoantes": 0}



# TESTE 6: palavra com acento/símbolo especial
# Justificativa: verifica que caracteres fora de a-z são ignorados

def test_caracter_especial():
    assert contar_letras("ação") == {"vogais": 1, "consoantes": 2}