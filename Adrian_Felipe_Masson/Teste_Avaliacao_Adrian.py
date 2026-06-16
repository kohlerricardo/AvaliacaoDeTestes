from AvaliacaoAdrian import calcular_situacao_aluno

def testar_calculo():
   
    
    resultado = calcular_situacao_aluno(8,8,8)
    assert resultado == "Aprovado",f"Erro, esperado 'Aprovado', recebido {resultado}"
        
    resultado = calcular_situacao_aluno(5,6,6)
    assert resultado == "Recuperação",f"Erro, esperado 'Recuperação', recebido {resultado}"
    
    resultado = calcular_situacao_aluno(4,3,4)
    assert resultado == "Reprovado",f"Erro, esperado 'Reprovado', recebido {resultado}"
        
    resultado = calcular_situacao_aluno(7,7,7)
    assert resultado == "Aprovado",f"Erro, esperado 'Aprovado', recebido {resultado}"

    resultado = calcular_situacao_aluno(5,5,5)
    assert resultado == "Recuperação",f"Erro, esperado 'Recuperação', recebido {resultado}"

    resultado = calcular_situacao_aluno(-2,5,8)
    assert resultado == ValueError ("Notas não podem ser negativas."),f"Erro, Esperado ValueError, recebido {resultado}"

testar_calculo()
