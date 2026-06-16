# Função para calcular o montante acumulado com juros compostos
def simular_rendimento(capital, taxa_mensal, meses):

    # Removido '=' para que capital zero seja aceito normalmente, mas capital negativo e meses negativos não sejam aceitos
    if capital < 0 or meses < 0:
        raise ValueError("Valores iniciais não podem negativos.")
    
    # formula para i ser a taxa mensal em decimal e tornar o calculo em codigo compatível        
    taxa_decimal = taxa_mensal / 100
    
    # formula para calcular o montante acumulado com juros compostos em formato de codigo
    montante = capital * (1 + taxa_decimal) ** meses
    
    # Mudando de 0 para 2 casas decimais paara ser compativel com o enunciado do teste

    return round(montante, 2)