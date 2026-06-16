#teste conforme plano_de_teste
from calculo_media import calcular_situacao_aluno

def teste_aprovado():
    assert calcular_situacao_aluno(8,8,8) == "Aprovado"

def teste_recuperacao():
    assert calcular_situacao_aluno(5,6,6) == "Recuperação"

def teste_reprovado():
    assert calcular_situacao_aluno(4,3,4) == "Reprovado"

def teste_aprovado():
    assert calcular_situacao_aluno(7,7,7) == "Aprovado"

def teste_nota_negativa():
    assert calcular_situacao_aluno(-2,5,8) == "ValueError"