def simular_rendimento(capital, taxa_mensal, meses):
    if capital <= 0 or meses < 0:
        raise ValueError("Valores iniciais não podem ser nulos ou negativos.")

    taxa_decimal = taxa_mensal / 100

    montante = capital * (1 + taxa_decimal) ** meses

    return round(montante, 2)


    # O código original utilizava round(montante, 0),ou seja, arredondava para 0 casas, mas é solicitado no
    #  enunicado que arredonde para 2 casas decimais por isso foi trocado o 0 pelo 2.


 