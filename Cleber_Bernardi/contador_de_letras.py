def contar_letras(palavra):
    resultado = {}
    vogais = 0
    consoantes = 0

    for letra in palavra:
        if letra in "0123456789" or letra == " ":
            continue
        elif letra in "aeiouAEIOU":
            vogais = vogais + 1
        else:
            consoantes = consoantes + 1

    resultado["vogais"] = vogais
    resultado["consoantes"] = consoantes

    return resultado
