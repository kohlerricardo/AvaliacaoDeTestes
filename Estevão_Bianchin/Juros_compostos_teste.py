import unittest
from juros_compostos import simular_rendimento


class TestSimularRendimento(unittest.TestCase):

    # Teste 1 - Caso normal
    def test_rendimento_normal(self):
        self.assertEqual(simular_rendimento(1000, 10, 2), 1210.0)

    # Teste 2 - Sem juros
    def test_sem_juros(self):
        self.assertEqual(simular_rendimento(1000, 0, 5), 1000.0)

    # Teste 3 - Zero meses
    def test_zero_meses(self):
        self.assertEqual(simular_rendimento(1000, 10, 0), 1000.0)

    # Teste 4 - Capital negativo
    def test_capital_negativo(self):
        with self.assertRaises(ValueError):
            simular_rendimento(-1000, 10, 5)

    # Teste 5 - Capital igual a zero
    def test_capital_zero(self):
        with self.assertRaises(ValueError):
            simular_rendimento(0, 10, 5)

    # Teste 6 - Meses negativos
    def test_meses_negativos(self):
        with self.assertRaises(ValueError):
            simular_rendimento(1000, 10, -5)


