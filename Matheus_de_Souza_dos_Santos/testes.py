from juros_compostos import simular_rendimento

def ct01():
     assert simular_rendimento(1000.0,1.0,12) == 1126.83, "Deu erro"

def ct02():
     assert simular_rendimento(500.0,2.0,3) == 530.60, "Deu erro"

def ct03():
     assert simular_rendimento(1000.0,5.0,0) == 1000.00, "Deu erro"
     
def ct04():
     assert simular_rendimento(-100.0,5.0,0) == 1000.00, "Deu erro"
    
ct01()
ct02()
ct03()
ct04()




# | ID   | Cenário                    | Tipo          | Entrada (cap, taxa, meses) | Resultado Esperado |
# | :--- | :---                       | :---          | :---                       | :---               |
# | CT01 | Rendimento padrão de 1 ano | Caminho Feliz | 1000.0, 1.0, 12            | `1126.83`          |
# | CT02 | Rendimento de curto prazo  | Caminho Feliz | 500.0, 2.0, 3              | `530.60`           |
# | CT03 | Zero meses de rendimento   | Borda         | 1000.0, 5.0, 0             | `1000.00`          |
# | CT04 | Capital negativo inserido  | Exceção       | -100.0, 1.0, 12            | Lança `ValueError` |
# | CT05 | Tempo negativo inserido    | Exceção       | 1000.0, 1.0, -5            | Lança `ValueError` |