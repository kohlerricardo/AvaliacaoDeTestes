def simular_rendimento(capital, taxa_mensal, meses):
    if capital <= 0 or meses < 0:
        raise ValueError("Valores iniciais não podem ser nulos ou negativos.")
        
    taxa_decimal = taxa_mensal / 100
    
    montante = capital * (1 + taxa_decimal) ** meses
    
    return round(montante, 0)


# Definir as credenciais 
capital = float(input("Digite o capital inicial: R$ "))
taxa_mensal = float(input("Digite a taxa de juros mensal (%): "))
meses = int(input("Digite o tempo em meses: "))


try: # Tentar executar o cálculo do rendimento

    # Chama a função que calcula os juros compostos
    resultado = simular_rendimento(capital, taxa_mensal, meses)
    print(f"Montante final: R$ {resultado}")

    # Captura erros do tipo ValueError gerados pela função
except ValueError as erro:
    print(f"Erro: {erro}") # Mensagem de erro 