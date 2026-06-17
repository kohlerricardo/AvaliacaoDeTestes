import pytest
from juros_compostos import simular_rendimento


def test_ct01_rendimento_padrao_1_ano():
    assert simular_rendimento(1000.0, 1.0, 12) == 1126.83


def test_ct02_rendimento_curto_prazo():
    assert simular_rendimento(500.0, 2.0, 3) == 530.60


def test_ct03_zero_meses():
    assert simular_rendimento(1000.0, 5.0, 0) == 1000.00


def test_ct04_capital_negativo():
    with pytest.raises(ValueError):
        simular_rendimento(-100.0, 1.0, 12)


def test_ct05_tempo_negativo():
    with pytest.raises(ValueError):
        simular_rendimento(1000.0, 1.0, -5)