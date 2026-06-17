def contar_letras(palavra):
    resultado = {}
#realocando as variaveis para fora do "for" para que o código funcione de fomra correta, pois se 
# ficasse dentro elas não guardariam valores    
    vogais = 0
    consoantes = 0

    for letra in palavra:
        
#Adicionei lower para que a string seja convertida em letras minusculas para não dar erro
#quando estiver misturado com letras maiusculas.

        if letra.lower() in "aeiou":
            vogais = vogais + 1
            
#Adicionei isalpha para que a contagem ignore os caracteres especiais e espaços. 
# git               
        elif letra.isalpha():
            consoantes = consoantes + 1

    resultado["vogais"] = vogais
    resultado["consoantes"] = consoantes
    return resultado

