#  import de função para o teste de juros compostos 
from juros_compostos import simular_rendimento

# Função para iniciar os testes conforme cenarios descritos no enunciado do teste
def testar_juros_compostos():
    print("Simulador de Rendimento com Juros Compostos")

    # Teste 01 - Rendimento padrão de 1 ano
    resultado = simular_rendimento(1000.0, 1.0, 12)
    assert resultado == 1126.83, f"Erro: Esperado 1126.83, recebido {resultado}"

    # Teste 02 - Rendimento de curto prazo
    resultado = simular_rendimento(500.0, 2.0, 3)
    assert resultado == 530.60, f"Erro: Esperado 530.60, recebido {resultado}"

    # Teste 03 - Zero meses de rendimento
    resultado = simular_rendimento(1000.0, 5.0, 0)
    assert resultado == 1000.00, f"Erro: Esperado 1000.00, recebido {resultado}"

    # Teste 04 - Capital negativo inserido
    try:
        simular_rendimento(-100.0, 1.0, 12)
        assert False, "Erro: Esperado ValueError para capital negativo, mas nenhuma exceção foi lançada."
    except ValueError:
        pass  # Exceção esperada, teste passou

    # Teste 05 - Tempo negativo inserido
    try:
        simular_rendimento(1000.0, 1.0, -5)
        assert False, "Erro: Esperado ValueError para tempo negativo, mas nenhuma exceção foi lançada."
    except ValueError:
        pass # Exceção esperada, teste passou

    print("Todos os testes passaram com sucesso!")

    #Teste 06 - capital igual a zero
    resultado = simular_rendimento(0.0, 1.0, 12)
    assert resultado == 0.00, f"Erro: Esperado 0.00, recebido {resultado}"
    
testar_juros_compostos()