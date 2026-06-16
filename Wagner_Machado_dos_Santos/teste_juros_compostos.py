#Situação Problema
# Uma calculadora de juros deve implementar uma função que calcula os juros compostos sobre um montante. A função recebe o capital inicial, uma taxa de juros mensal (em porcentagem) e o tempo em meses. O sistema deve retornar o montante final utilizando a fórmula de juros compostos: 
# M
# =
# C
# ×
# (
# 1
# +
# i
# )
# t
# . O resultado deve ser arredondado para 2 casas decimais.

# Plano de Teste: Simulador de RendimentosPlano de Teste: Simulador de Rendimentos
# ID	Cenário	Tipo	Entrada (cap, taxa, meses)	Resultado Esperado
# CT01	Rendimento padrão de 1 ano	Caminho Feliz	1000.0, 1.0, 12	1126.83
# CT02	Rendimento de curto prazo	Caminho Feliz	500.0, 2.0, 3	530.60
# CT03	Zero meses de rendimento	Borda	1000.0, 5.0, 0	1000.00
# CT04	Capital negativo inserido	Exceção	-100.0, 1.0, 12	Lança ValueError
# CT05	Tempo negativo inserido	Exceção	1000.0, 1.0, -5	Lança ValueError
# # com esse exemplo de codigos testes from ex_04 import quadrante

# def testar_quadrante():
#     resultado = quadrante(1, 1)
#     assert resultado == "O ponto (1, 1) está no 1º quadrante",f"Erro: Esperado 'O ponto (1, 1) está no 1º quadrante', recebido {resultado}"
#     resultado = quadrante(-1, 1)
#     assert resultado == "O ponto (-1, 1) está no 2º quadrante",f"Erro: Esperado 'O ponto (-1, 1) está no 2º quadrante', recebido {resultado}"
#     resultado = quadrante(-1, -1)
#     assert resultado == "O ponto (-1, -1) está no 3º quadrante",f"Erro: Esperado 'O ponto (-1, -1) está no 3º quadrante', recebido {resultado}"
#     resultado = quadrante(1, -1)
#     assert resultado == "O ponto (1, -1) está no 4º quadrante",f"Erro: Esperado 'O ponto (1, -1) está no 4º quadrante', recebido {resultado}"

#     resultado = quadrante(0, 1)
#     assert resultado == "O ponto (0, 1) está sobre o eixo y",f"Erro: Esperado 'O ponto (0, 1) está sobre o eixo y', recebido {resultado}"

#     resultado = quadrante(1, 0)
#     assert resultado == "O ponto (1, 0) está sobre o eixo x",f"Erro: Esperado 'O ponto (1, 0) está sobre o eixo x', recebido {resultado}"

#     resultado = quadrante(0, 1)
#     assert resultado == "O ponto (0, 0) está na origem",f"Erro: Esperado 'O ponto (0, 0) está na origem', recebido {resultado}"
#     print("Todos os teste passaram com sucesso!")
# testar_quadrante()

#  import de funçõa para o teste de juros compostos 

from juros_compostos import simular_rendimento

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

    #Teste 06 - capital igual a zero
    resultado = simular_rendimento(0.0, 1.0, 12)
    assert resultado == 0.00, f"Erro: Esperado 0.00, recebido {resultado}"

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

testar_juros_compostos()