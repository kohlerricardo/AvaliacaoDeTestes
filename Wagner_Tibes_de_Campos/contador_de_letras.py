def contar_letras(palavra):
    resultado = {}
    vogais = 0 #variaveis tem que ser antes do for 
    consoantes = 0 #variaveis tem que ser antes do for se nao cria um laço infinito.

    for letra in palavra.lower(): #Alteração feito por que sem esse .lower deixa toda palavra em minuscolo
     if letra.isalpha(): #alteração feita para ignorar numeros.
        if letra in "aeiou":
            vogais = vogais + 1
        else:
            consoantes = consoantes + 1
    resultado["vogais"] = vogais
    resultado["consoantes"] = consoantes
    return resultado

meu_resultado = contar_letras ("")
#print (meu_resultado)
