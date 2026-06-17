from contador_de_letras import contar_letras


def teste_contador_letras ():
    
    vogais = 0 
    consoantes = 0

    resultado = contar_letras  
    assert contar_letras ("teste") == {"vogais": 2, "consoantes": 3} 

    resultado = contar_letras
    assert contar_letras ("ALUNO") == {"vogais": 3, "consoantes": 2}

    resultado = contar_letras
    assert contar_letras ("senha 123") == {"vogais": 2, "consoantes": 3}
    
    resultado = contar_letras
    assert contar_letras ("aeiou") == {"vogais": 5, "consoantes": 0}

    resultado = contar_letras
    assert contar_letras ("") == {"vogais": 0, "consoantes": 0}


teste_contador_letras()  




    