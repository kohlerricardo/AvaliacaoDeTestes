from calculo_media import calcular_situacao_aluno

def teste_sistema_aprovacao():
   
    cenarios = {
        'CT01': (8.0, 8.0, 8.0, "Aprovado"),
        'CT02': (5.0, 6.0, 6.0, "Recuperação"),
        'CT03': (4.0, 3.0, 4.0, "Reprovado"),
        'CT04': (7.0, 7.0, 7.0, "Aprovado"),
        'CT05': (5.0, 5.0, 5.0, "Recuperação"),
        'CT06': (-2.0, 5.0, 8.0, "Exceção")
    }

    n1, n2, n3, esperado = cenarios['CT01']
    resultado = calcular_situacao_aluno (n1,n2,n3)
    assert resultado ==  esperado, f"Erro no CT01: recebido {resultado}"
    n1, n2, n3, esperado = cenarios['CT02']
    resultado = calcular_situacao_aluno (n1,n2,n3)
    assert resultado == esperado, f"Erro no CT02: recebido {resultado}"
    n1, n2, n3, esperado = cenarios['CT03']
    resultado = calcular_situacao_aluno (n1,n2,n3)
    assert resultado == esperado, f"Erro no CT03: recebido {resultado}"
    n1, n2, n3, esperado = cenarios['CT04']
    resultado = calcular_situacao_aluno (n1,n2,n3)
    assert resultado == esperado, f"Erro no CT04: recebido {resultado}"
    n1, n2, n3, esperado = cenarios['CT05']
    resultado = calcular_situacao_aluno (n1,n2,n3)
    assert resultado == esperado, f"Erro no CT05: recebido {resultado}"
    try:
        calcular_situacao_aluno(-2.0, 5.0, 8.0)
        
        assert False, "Erro no CT06: O sistema aceitou nota negativa!"
    except ValueError:
        
        pass

    teste_sistema_aprovacao()



