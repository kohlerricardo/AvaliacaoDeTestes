from calculo_media import calcular_situacao_aluno

def teste_de_aprovacao():

    resultado = calcular_situacao_aluno(8.0, 8.0, 8.0)
    assert resultado == "Aprovado", f"CT01 falhou: Resultado {resultado}, esperado 'Aprovado'"

    resultado = calcular_situacao_aluno(5.0, 6.0, 6.0)
    assert resultado == "Recuperação", f"CT02 falhou: Resultado {resultado}, esperado 'Recuperação'"

    resultado = calcular_situacao_aluno(4.0, 3.0, 4.0)
    assert resultado == "Reprovado", f"CT03 falhou: Resultado {resultado}, esperado 'Reprovado'"

    resultado = calcular_situacao_aluno(7.0, 7.0, 7.0)
    assert resultado == "Aprovado", f"CT04 falhou: Resultado {resultado}, esperado 'Aprovado'"

    resultado = calcular_situacao_aluno(5.0, 5.0, 5.0)
    assert resultado == "Recuperação", f"CT05 falhou: Resultado {resultado}, esperado 'Recuperação'"

    try:
        calcular_situacao_aluno(-2.0, 5.0, 8.0)
        assert False, "O sistema não aceita notas negativas."
    except ValueError:
        print("Excessão, erro")

teste_de_aprovacao()
