import unittest
from provacorreção import calcular_situacao_aluno  # ajuste para o nome do seu arquivo



class TestCalcularSituacaoAluno(unittest.TestCase):

    # CT01 - Aluno aprovado com folga
    def test_aprovado_com_folga(self):
        media, situacao = calcular_situacao_aluno(8.0, 8.0, 8.0)
        self.assertEqual(situacao, "Aprovado")

    # CT02 - Aluno em recuperação
    def test_recuperacao(self):
        media, situacao = calcular_situacao_aluno(5.0, 6.0, 6.0)
        self.assertEqual(situacao, "Recuperação")

    # CT03 - Aluno reprovado
    def test_reprovado(self):
        media, situacao = calcular_situacao_aluno(4.0, 3.0, 4.0)
        self.assertEqual(situacao, "Reprovado")

    # CT04 - Nota de corte para aprovado
    def test_aprovado_nota_corte(self):
        media, situacao = calcular_situacao_aluno(7.0, 7.0, 7.0)
        self.assertEqual(situacao, "Aprovado")

    # CT05 - Nota de corte para recuperação
    def test_recuperacao_nota_corte(self):
        media, situacao = calcular_situacao_aluno(5.0, 5.0, 5.0)
        self.assertEqual(situacao, "Recuperação")

    # CT06 - Nota negativa
    def test_nota_negativa(self):
        with self.assertRaises(ValueError):
            calcular_situacao_aluno(-2.0, 5.0, 8.0)


if __name__ == "__main__":
    unittest.main()