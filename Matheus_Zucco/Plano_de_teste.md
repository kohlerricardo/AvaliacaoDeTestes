# Situação Problema
Uma calculadora de juros deve implementar uma função que calcula os juros compostos sobre um montante. A função recebe o capital inicial, uma taxa de juros mensal (em porcentagem) e o tempo em meses. O sistema deve retornar o montante final utilizando a fórmula de juros compostos: $M = C \times (1 + i)^t$. O resultado deve ser arredondado para 2 casas decimais.

## Plano de Teste: Simulador de Rendimentos

| ID | Cenário | Tipo | Entrada (cap, taxa, meses) | Resultado Esperado |
| :--- | :--- | :--- | :--- | :--- |
| CT01 | Rendimento padrão de 1 ano | Caminho Feliz | 1000.0, 1.0, 12 | `1126.83` |
| CT02 | Rendimento de curto prazo | Caminho Feliz | 500.0, 2.0, 3 | `530.60` |
| CT03 | Zero meses de rendimento | Borda | 1000.0, 5.0, 0 | `1000.00` |
| CT04 | Capital negativo inserido | Exceção | -100.0, 1.0, 12 | Lança `ValueError` |
| CT05 | Tempo negativo inserido | Exceção | 1000.0, 1.0, -5 | Lança `ValueError` |