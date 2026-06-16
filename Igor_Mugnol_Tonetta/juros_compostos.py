def simular_rendimento(capital, taxa_mensal, meses):
    if capital <= 0 or meses < 0:
        raise ValueError("Valores iniciais não podem ser nulos ou negativos.")
        
    taxa_decimal = taxa_mensal / 100
    
    montante = capital * (1 + taxa_decimal) ** meses
    
    return round(montante, 0)