# Situação problema 

O sistema deve calcular a média ponderada de três notas (pesos 2, 3 e 5, respectivamente) e retornar a situação do aluno. Regras: Média > 7.0 (Aprovado), entre 5.0 e 6.9 (Recuperação), e < 5.0 (Reprovado). As notas informadas devem estar entre 0 e 10.
## Plano de Teste: Sistema de Aprovação

| ID | Cenário | Tipo | Entrada (n1, n2, n3) | Resultado Esperado |
| :--- | :--- | :--- | :--- | :--- |
| CT01 | Aluno Aprovado com folga | Caminho Feliz | 8.0, 8.0, 8.0 | "Aprovado" |
| CT02 | Aluno em Recuperação | Caminho Feliz | 5.0, 6.0, 6.0 | "Recuperação" |
| CT03 | Aluno Reprovado | Caminho Feliz | 4.0, 3.0, 4.0 | "Reprovado" |
| CT04 | Exatamente na nota de corte (Aprovado) | Borda | 7.0, 7.0, 7.0 | "Aprovado" |
| CT05 | Exatamente na nota de corte (Recuperação) | Borda | 5.0, 5.0, 5.0 | "Recuperação" |
| CT06 | Nota negativa inserida | Exceção | -2.0, 5.0, 8.0 | Lança `ValueError` |