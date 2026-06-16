def simular_rendimento(capital, taxa_mensal, meses):
    if capital <= 0 or meses < 0:
        raise ValueError("Valores iniciais não podem ser nulos ou negativos.")
        
    taxa_decimal = taxa_mensal / 100
    
    montante = capital * (1 + taxa_decimal) ** meses
    #mudei o 0 pelo 2, pois o 0 fazia com que os valores "não tivessem casas decimais", arredondando o valor 
    return round(montante, 2)
