def contar_letras(palavra):

    # Os contadores foram movidos para fora do for,
    # pois dentro do for eram zerados a cada repetição.
    vogais = 0
    consoantes = 0

    # Foi adicionado .lower() para que letras maiúsculas
    # também sejam reconhecidas corretamente.
    for letra in palavra.lower():

        # Se a letra for uma vogal, incrementa o contador.
        if letra in "aeiou":
            vogais += 1

    # Verifica se o caractere está entre "a" e "z",
    # garantindo que apenas letras sejam contadas como consoantes,
    # enquanto números, espaços e símbolos são ignorados.
        elif "a" <= letra <= "z":
             consoantes += 1

    # Retorna um dicionário com as quantidades encontradas.
    return {
        "vogais": vogais,
        "consoantes": consoantes
    }

# Adicionado input para permitir que o usuário digite a palavra.
palavra = input("Digite uma palavra: ")

# Chama a função passando a palavra digitada.
resultado = contar_letras(palavra)

# Exibe o resultado da contagem.
print(resultado)