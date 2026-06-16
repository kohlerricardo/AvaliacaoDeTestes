def contar_letras(palavra):
    resultado = {}
    vogais = 0
    consoantes = 0

    for letra in palavra.lower():
        if letra in "aeiou":
            vogais += 1
        elif letra.isalpha(): 
            consoantes += 1

    resultado["vogais"] = vogais
    resultado["consoantes"] = consoantes
    return resultado