def contar_letras(palavra):
    resultado = {}

    # Variáveis: vogais e consoantes retiradas de dentro do laço FOR para o topo da função,
    # assim subindo o escopo para que possam ser utilizadas fora do laço FOR.
    vogais = 0
    consoantes = 0

    for letra in palavra:
        # Condição para comparar se o caractere é um algarismo ou espaço.
        if letra in "0123456789" or letra == " ":
            continue
        # Adicionadas as vogais maiúsculas para comparação.
        elif letra in "aeiouAEIOU":
            vogais = vogais + 1
        else:
            consoantes = consoantes + 1

    resultado["vogais"] = vogais
    resultado["consoantes"] = consoantes

    return resultado
