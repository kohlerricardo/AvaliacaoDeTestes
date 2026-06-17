def contar_letras(palavra):
    palavra = palavra.lower()
    vogais = 0
    consoantes = 0
    if not palavra or palavra.strip() == "":
        return {"vogais": 0, "consoantes": 0}
    for letra in palavra:
        if letra.isalpha():
            if letra in "aeiou":
                
                vogais = vogais + 1
            else:
                consoantes = consoantes + 1
            resultado = {}
    resultado["vogais"] = vogais
    resultado["consoantes"] = consoantes
    return resultado