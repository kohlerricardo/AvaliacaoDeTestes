# M = Montante 
# C = Capital inicial 
# i = Taxa de juros 
# t = Tempo


def simular_rendimento(capital, taxa_mensal, meses):
    if capital <= 0 or meses < 0:
        raise ValueError("Valores iniciais não podem ser nulos ou negativos.")
        
    taxa_decimal = taxa_mensal / 100
    
    montante = capital * (1 + taxa_decimal) ** meses
    
    return round(montante, 2)#ajustei o round por que estava arredondando pra zero casas decimais

# print(simular_rendimento(1000.0,1.0,12))
# print(simular_rendimento(500.0,2.0,3))
# # print(simular_rendimento(1000.0,5.0,0))
# # print(simular_rendimento(-1000.0,1.0,-5))