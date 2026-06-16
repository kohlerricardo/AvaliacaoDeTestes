# Situação Problema

Uma função deve receber uma palavra sem acentos e retornar um dicionário contendo a quantidade exata de vogais e de consoantes. Caracteres numéricos ou especiais devem ser ignorados na contagem.

## Plano de Teste: Analisador de Letras

| ID | Cenário | Tipo | Entrada (palavra) | Resultado Esperado |
| :--- | :--- | :--- | :--- | :--- |
| CT01 | Palavra comum em minúsculas | Caminho Feliz | "teste" | `{"vogais": 2, "consoantes": 3}` |
| CT02 | Palavra com maiúsculas e minúsculas | Caminho Feliz | "ALUNO" | `{"vogais": 3, "consoantes": 2}` |
| CT03 | String contendo números e espaços | Borda | "senha 123" | `{"vogais": 2, "consoantes": 3}` |
| CT04 | Palavra sem consoantes | Borda | "aeiou" | `{"vogais": 5, "consoantes": 0}` |
| CT05 | String vazia | Borda | "" | `{"vogais": 0, "consoantes": 0}` |