    print ("Digite uma palvra: ")
    def contar_letras(palavra):
        resultado = {}
        for letra in palavra:
            vogais = 0
            consoantes = 0
            if letra in "aeiou":
                vogais = vogais + 1
            else:
                consoantes = consoantes + 1
        resultado["vogais"] = vogais
        resultado["consoantes"] = consoantes
        return resultado