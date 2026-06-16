from juros_compostos import simular_rendimento

def caso1():

    resultado = simular_rendimento (1000.0, 1.0, 12)
    assert resultado == 1126.83, f"Erro na operação, esperado 1126.83, recebido {resultado}"

def caso2():

    resultado = simular_rendimento (500.0, 2.0, 3)
    assert resultado == 530.60, f"Erro na operação, esperado 530.60, recebido {resultado}"

def caso3():

    resultado = simular_rendimento (1000.0, 5.0, 0)
    assert resultado == 1000.0, f"Erro na operação, esperado 1000.0, recebido {resultado}"

def caso4():
    
    try:
        simular_rendimento (-100.0, 1.0, 12)
        assert False, "Era esperado um ValueError"

    except ValueError:
        assert True

def caso5():

    try:
        simular_rendimento (100.0, 1.0, -12)
        assert False, "Era esperado um ValueError"

    except ValueError:
        assert True

caso1()
caso2()
caso3()
caso4()
caso5()

print("todos os testes passaram, parabens")