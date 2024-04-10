def gerador_senha(tamanho_da_senha: int):
    # Verifica se o parâmetro é um número inteiro
    try:
        tamanho_da_senha = int(tamanho_da_senha)
        if tamanho_da_senha >= 4: 
            # Importa as bibliotecas necessárias
            import string
            from random import shuffle
            from random import choice, choices
            # Gera a senha com no mínimo 4 caractéres
            senha = [
                choice(string.digits),
                choice(string.ascii_uppercase),
                choice(string.ascii_lowercase),
                choice(string.punctuation),
            ]
            # Preenche os demais caracteres da senha (caso maior que 4) com caracteres aleatórios
            possibilidades = ''.join([string.ascii_letters, string.digits, string.punctuation])
            senha.extend(choices(possibilidades, k=tamanho_da_senha - 4))
            # Embaralha os caracteres da lista da senha
            shuffle(senha)
            # Junta os caracteres da lista em uma única string
            senha_gerada = "".join(senha)
            # Retorna o valor da função (a senha)
            return senha_gerada
        else:
            print('O tamanho da senha não pode ser menor do que 4 caractéres')
    except:
        raise ValueError('É necessário um número inteiro para o tamanho da senha')
    
tamanho_senha = int(input("Digite um valor maior do que 3 pra gerar a senha: "))
print(gerador_senha(tamanho_da_senha=tamanho_senha))
