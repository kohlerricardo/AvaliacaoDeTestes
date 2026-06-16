from contador_de_letras import contar_letras


def teste_contador_de_letras():

    def comum_minusculas():
        """| CT01 | Palavra comum em minúsculas | Caminho Feliz | "teste" | `{"vogais": 2, "consoantes": 3}` |"""
        expected_vowels, expected_consonants = 2, 3

        result = contar_letras("teste")
        result_vowels, result_consonants = result.values()

        assert result_vowels == expected_vowels, (
            f"Esperando vogais: {expected_vowels}, recebido: {result_vowels}"
        )
        assert result_consonants == expected_consonants, (
            f"Esperando consoantes: {expected_consonants}, recebido: {result_consonants}"
        )

    def maiusculas_minusculas():
        """| CT02 | Palavra com maiúsculas e minúsculas | Caminho Feliz | "ALUNO" | `{"vogais": 3, "consoantes": 2}` |"""
        expected_vowels, expected_consonants = 3, 2

        result = contar_letras("ALUNO")
        result_vowels, result_consonants = result.values()

        assert result_vowels == expected_vowels, (
            f"Esperando vogais: {expected_vowels}, recebido: {result_vowels}"
        )
        assert result_consonants == expected_consonants, (
            f"Esperando consoantes: {expected_consonants}, recebido: {result_consonants}"
        )

    def numeros_espacos():
        """| CT03 | String contendo números e espaços | Borda | "senha 123" | `{"vogais": 2, "consoantes": 3}` |"""
        expected_vowels, expected_consonants = 2, 3

        result = contar_letras("senha 123")
        result_vowels, result_consonants = result.values()

        assert result_vowels == expected_vowels, (
            f"Esperando vogais: {expected_vowels}, recebido: {result_vowels}"
        )
        assert result_consonants == expected_consonants, (
            f"Esperando consoantes: {expected_consonants}, recebido: {result_consonants}"
        )

    def sem_consoantes():
        """| CT04 | Palavra sem consoantes | Borda | "aeiou" | `{"vogais": 5, "consoantes": 0}` |"""
        expected_vowels, expected_consonants = 5, 0

        result = contar_letras("aeiou")
        result_vowels, result_consonants = result.values()

        assert result_vowels == expected_vowels, (
            f"Esperando vogais: {expected_vowels}, recebido: {result_vowels}"
        )
        assert result_consonants == expected_consonants, (
            f"Esperando consoantes: {expected_consonants}, recebido: {result_consonants}"
        )

    def string_vazia():
        """| CT05 | String vazia | Borda | "" | `{"vogais": 0, "consoantes": 0}` |"""
        expected_vowels, expected_consonants = 0, 0

        result = contar_letras("")
        result_vowels, result_consonants = result.values()

        assert result_vowels == expected_vowels, (
            f"Esperando vogais: {expected_vowels}, recebido: {result_vowels}"
        )
        assert result_consonants == expected_consonants, (
            f"Esperando consoantes: {expected_consonants}, recebido: {result_consonants}"
        )

    comum_minusculas()
    maiusculas_minusculas()
    numeros_espacos()
    sem_consoantes()
    string_vazia()


teste_contador_de_letras()
